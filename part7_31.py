from datetime import datetime

def calc_diff (day: int, month: int, year: int) :
    bday = datetime (day = day, month = month, year = year)
    mill = datetime (day = 31, month = 12, year = 1999)

    if mill > bday :
        diff = mill - bday
        print (f"You were {diff.days} days old when the eve of new millenia happened")
    elif mill == bday :
        print ("You were born on the eve of the new millenia day")  
    else :
        print ("You were not born before or on the eve of the new millenia day")

day = int (input ("Day: "))
month = int (input ("Month: "))
year = int (input ("Year: "))

calc_diff (day, month, year)