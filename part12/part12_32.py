class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return (
            f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
        )

def names_of_students (attempt: list) :
    mp_obj = map (lambda x : x.student_name, attempt)

    return list (mp_obj)

def course_names (attempt: list) :
    mp_obj = set (map (lambda x : x.course_name, attempt))

    return sorted (list (mp_obj))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)

print ("\nCourses :: \n")
for name in course_names([s1, s2, s3]):
    print(name)