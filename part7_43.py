import csv
from datetime import datetime, timedelta

def cheaters () :
    start = open ("start_times.csv", "r")
    sub_t = open ("submissions.csv", "r")
    stud = {}

    for line in csv.reader(start, delimiter = ";") :
        student = line[0]
        start_time = datetime.strptime(line[1], "%H:%M")
        stud[student] = {
            "start_time": start_time,
            "stats" : {"tasks": [], "points": [], "submissions": []}
        }
        
    for line in csv.reader (sub_t, delimiter = ";") :
        
        student = line [0]
        task_no = line [1]
        points = line[2]
        sub_time = datetime.strptime (line[3], "%H:%M")  

        if student not in stud :
            continue  

        if sub_time > stud[student]["start_time"] + timedelta (hours = 3, minutes = 0) :
                continue          

        elif task_no in stud[student]["stats"]["tasks"] :            
            idx = stud[student]["stats"]["tasks"].index (task_no)
            if points > stud[student]["stats"]["points"][idx] :
                stud[student]["stats"]["tasks"][idx] = task_no
                stud[student]["stats"]["points"][idx] = points
                stud[student]["stats"]["submissions"][idx] = sub_time

        else :            
            stud[student]["stats"]["tasks"].append (task_no)
            stud[student]["stats"]["points"].append (points)
            stud[student]["stats"]["submissions"].append(sub_time)


        stud_fin = {}

        for student in stud :
            task_list = stud[student]["stats"]["tasks"]
            point_list = stud[student]["stats"]["points"]
            point_list = [int(x) for x in point_list]
            total = sum (point_list)
            stud_fin[student] = {
                "tasks" : task_list,
                "points" : point_list,
                "total" : total
            }
    
    #print (stud)
    return stud_fin    


if __name__ == "__main__" :
    ret = cheaters()
    for student in ret :
        print (f"{student} : {ret[student]["total"]}")
    
    # if "tiina" in ret :
    #     print (ret["tiina"]["tasks"])
    #     print (ret["tiina"]["points"])
    # import timeit
    # print(timeit.timeit("cheaters", setup="from __main__ import cheaters"))

# For 'tiina' from testsol.py = 
# tasks = ['7', '4', '8', '1', '4', '6', '5', '7', '5', '6', '2', 
#           '7', '8', '1', '4', '4', '1', '8', '1', '5', '1', '8', 
#           '2', '5', '6', '6', '4', '5', '1', '2', '2', '2', '1', 
#           '3', '5', '7']

# points = ['0', '3', '5', '2', '0', '1', '6', '3', '5', '5', '3', 
#           '2', '4', '0', '3', '0', '6', '2', '1', '2', '0', '0', 
#           '6', '2', '2', '6', '6', '2', '1', '5', '3', '2', '2', 
#           '1', '3', '4']

# For 'tiina' from our solution:
#
# tasks = ['7', '8', '1', '4', '6', '5', '2', '3']
# points= [4,    5,   6,   6,   6,   6,   6,   1]

###### FIXEDDDDDD!!!! ########

