def take_input () -> list :
    inputs = []

    inp = input ("Exam points and exercises completed: ")

    while inp != "" :
        inputs.append(inp)
        inp = input ("Exam points and exercises completed: ")

    # print (inputs)

    return inputs

def seperate_input (inputs) :
    stud_marks = []
    grade = [0] * 6
    sum_grade = 0
    size = len(inputs)

    for i in range (0, size) :
        stud_marks = inputs[i].split (" ")

        exam = int (stud_marks[0])
        cour = int (stud_marks[1])

        cour = cour // 10
        total = cour + exam
        sum_grade += total

        if exam < 10 :
            grade[0] += 1
            continue        

        if total >= 0 and total <= 14 :
            grade[0] += 1

        elif total >= 15 and total <= 17 :
            grade[1] += 1

        elif total >= 18 and total <= 20 :
            grade[2] += 1

        elif total >= 21 and total <= 23 :
            grade[3] += 1
        
        elif total >= 24 and total <= 27 :
            grade[4] += 1

        else :
            grade[5] += 1

    print (f"Points average : {sum_grade / size :.1f}")
    print (f"Pass Percentage: {((size - grade[0]) / size) * 100.0 :.1f}") 

    print ("Grade Distribution: ")
    for i in range (5, -1, -1) :        
        stars = "*" * grade[i]
        print (f"  {i} : {stars}")              

    
def main () :
    inputs = take_input ()
    seperate_input (inputs)

main()
