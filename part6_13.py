if __name__ == "__main__" :
    if False:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
        # hard-coded input
        student_info = "students.txt"
        exercise_data = "exercises.txt"
    
    student_names = {}
    total = {}

    with open(student_info) as students :
        for line in students :
            line = line.replace ("\n", "")
            parts = line.split(";")

            if parts[0] == "id" :
                continue

            student_names[parts[0]] = f"{parts[1]} {parts[2]}"

    student_marks = {}
    with open(exercise_data) as exercises :
        for line in exercises :
            parts = line.split(";")

            if parts[0] == "id" :
                continue
            
            length = len (parts)
            i = 1
            sum = 0
            while i < length :
                sum += int(parts[i])
                i += 1

            student_marks[parts[0]] = sum
    

    # print (student_names)
    # print (student_marks)

    # for id, name in student_names.items() :
    #     if id in student_marks :
    #         print (f"{name} {student_marks[id]}")

    exam = {}

    with open ("exam.txt") as exams :
        for line in exams :
            line = line.replace ("\n", "")

            parts = line.split (";")

            if parts[0] == "id" :
                continue

            length = len (parts)
            i = 1
            sum = 0
            while i < length :
                sum += int(parts[i])
                i += 1

            exam[parts[0]] = sum

    
    #print (exam)

    for id, marks in exam.items() :
        if id in student_marks :
            total[id] = marks + (student_marks[id] // 4)

    
    print (total)

    #AFTER THIS THERE ARE BORING IF-ELIF conditions

    
