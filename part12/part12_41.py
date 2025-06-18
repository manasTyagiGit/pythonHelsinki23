import re

def is_dotw (day: str) :
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for name in week :
        if re.search (day, name) :
            return True
        
    return False

def all_vowels (inp: str) :
    for c in inp :
        if re.search("[AEIOUaeiou]", c) :
            continue
        else :
            return False
        
    return True

def time_of_day (inp_time: str) :
    if re.search ("^([0-1][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]$", inp_time) :
        return True
    
    return False


print(time_of_day("12:43:01"))
print(time_of_day("AB:01:CD"))
print(time_of_day("17:59:59"))
print(time_of_day("33:66:77"))