import csv
from datetime import datetime, timedelta

def cheaters () :
    cheater = []

    start = open ("start_times.csv",  "r")
    sub_t = open ("submissions.csv", "r")

    s_time = {}
    last_sub_t = {}

    for line in csv.reader (start, delimiter = ";") :
        s_time[line[0]] = datetime.strptime (line[1], "%H:%M")

    for line in csv.reader (sub_t, delimiter = ";") :
        sub_time = datetime.strptime (line[3], "%H:%M")
        if line[0] not in last_sub_t :
            last_sub_t[line[0]] = sub_time

        else :
            if last_sub_t[line[0]] < sub_time :
                last_sub_t[line[0]] = sub_time

    # print (s_time)
    # print (last_sub_t)  
    # 

    for student in last_sub_t :
        if last_sub_t[student] > s_time[student] + timedelta(hours=3) :
            cheater.append(student)  

    return cheater

if __name__ == "__main__" :
    import timeit
    print(timeit.timeit("cheaters", setup="from __main__ import cheaters"))

    