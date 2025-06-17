class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return (
            f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
        )

def accepted (students: list) :
    flt = filter (lambda x : x.grade >= 1, students)

    return list (flt)

def attempts_with_grade (students: list, threshold: int):
    flt = filter (lambda x : x.grade == threshold, students)

    return list (flt) 

def passed_students (students: list, course: str) :
    flt = list (filter (lambda x : x.course_name == course and x.grade >= 0, students))
    mp = map (lambda x: x.student_name, flt)

    return sorted(list(mp))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
    print(attempt)