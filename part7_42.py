import urllib.request
import json

def retrive_all () -> list :
    my_request = urllib.request.urlopen ("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    data = json.loads(data) 

    ret_list = []

    for dict in data :
        if dict["enabled"] :
            app_tuple = (dict["fullName"], dict["name"], dict["year"], sum(dict["exercises"]))
            ret_list.append(app_tuple)

    return ret_list

def retrieve_course (course_name: str) -> dict :

    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    my_request = urllib.request.urlopen (url)
    data = my_request.read()
    data = json.loads(data)

    print (data)

    ret_dict = {}

    ret_dict['weeks'] = len (data)
    max_stud = -1
    hour = 0
    exer_total = 0
    
    for week, docs in data.items() :
        if docs['students'] > max_stud :
            max_stud = docs['students']

        hour += docs['hour_total']
        exer_total += docs['exercise_total']
        

    ret_dict['students'] = max_stud
    ret_dict['hours'] = hour
    ret_dict['hours_average'] = hour // max_stud

    ret_dict['exercises'] = exer_total
    ret_dict['exercies_average'] = exer_total // max_stud

    return ret_dict

if __name__ == "__main__" :
    # course_active = retrive_all()

    # for tup in course_active :
    #     print (tup) 

    ret = retrieve_course("docker2019")

    print (ret)


