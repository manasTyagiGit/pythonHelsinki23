import string

def is_it_valid (inp: str) -> bool :
    
    # sample string = 310823A9877

    if inp[6] != '+' and inp[6] != '-' and inp[6] != 'A' :        # CENTURY MARKER
        return False

    day = int(inp[0:2])
    month = int (inp[2:4])
    year = int (inp[4:6])

    # print (f"{day}:{month}:{year}")

    if month > 12 :         return False

    if month == 2 and (day != 28 or day != 29) :
        return False
    
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day != 30 :
        return False
    
    elif day != 31 :
        return False
    
    childString = "0123456789"
    childString += string.ascii_uppercase

    contCheckStr = inp[0:6] + inp[7:10]
    contCheckStr = int (contCheckStr)

    rem = contCheckStr % 31

    controlChar = childString[rem]

    if controlChar != inp[10] :
        return False    

    return True


inp = input ("Enter your PIC to validate : ")

print (is_it_valid (inp))