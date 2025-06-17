from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
    

def sum_of_all_credits (courses: list) :
    sum_creds = reduce (lambda cur, obj : cur + obj.credits, courses, 0)

    return sum_creds

def sum_of_passed_credits (courses: list) :
    sum_creds = reduce (lambda cur, obj : cur + obj.credits, filter (lambda obj: obj.grade >= 1, courses), 0)

    return sum_creds

def average (courses: list) :
    sum_creds = reduce (lambda cur, obj : cur + obj.grade, filter (lambda obj : obj.grade >= 1, courses), 0)

    return sum_creds / len (list(filter(lambda obj : obj.grade >= 1, courses)))
    
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
ag = average([s1, s2, s3])
print(ag)