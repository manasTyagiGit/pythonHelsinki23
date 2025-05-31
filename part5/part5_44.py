def add_student (students : dict, name : str) :
    students[name] = []
    

def print_student (students : dict, name : str) :
    if name in students :
        print (f"{name} : {students[name]}")

    else :
        print (f"{name} : No such student")

def found_positive (course : tuple, courses : list) :
    for i in courses :
        if i[0] == course[0] :
            if i[1] > course[1] :
                return False        

    return True

def add_course (students : dict, name : str, course : tuple) :
    if name in students : 
        if course[1] > 0 :   
            if found_positive (course, students[name]) :    
                students[name].append (course)
        
if __name__ == "__main__" :
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")