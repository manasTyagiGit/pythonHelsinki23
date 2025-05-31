from datetime import *

def run_pgm () :
    file_name = input ("Filename: ")

    file_head = open (file_name, "w")

    start_day = input ("Starting date: ")
    day = int (input ("How many days?: "))

    act_start_day = datetime.strptime (start_day, "%d.%m.%Y")
    
    end = act_start_day + timedelta(days = day - 1) 

    file_head.write (f"Time period: {act_start_day.strftime("%d.%m.%Y")}-{end.strftime("%d.%m.%Y")}\n")  

    print ("Please type in screen time in minutes on each day (TV computer mobile):")

    st_dict = {}
    total_time = 0    

    for i in range(day):

        cur_day = datetime.strftime(act_start_day + timedelta (days = i), "%d.%m.%Y")
        cur_line = input (f"Screen time {cur_day}: ")

        cur_line_list = cur_line.split(" ")

        cur_line_list = [int(x) for x in cur_line_list]            

        st_dict[cur_day] = cur_line_list

        total_time += sum(cur_line_list)        

    if day != 0 :
        avg_time = total_time / day

    file_head.write (f"Total minutes: {total_time}\nAverage minutes: {avg_time}\n")

    for key, value in st_dict.items() :
        file_head.write(f"{key} :")
        file_head.write(f"{value[0]}")

        for x in value[1:] : 
            file_head.write (f"/{x}")

        file_head.write("\n")    

    
if __name__ == "__main__" :
    run_pgm()