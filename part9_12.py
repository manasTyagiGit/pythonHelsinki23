class ExamSubmission :
    def __init__ (self, examinee: str, points: int) :
        self.examinee = examinee
        self.points   = points

    def get_examinee(self) :
        return self.examinee
    
    def get_points(self) :
        return self.points  

    def __str__ (self) :
        return f"ExamSubmission (examinee {self.get_examinee()}, points: {self.get_points()})"  

def passed (submissions: list, lowest_passing: int) :
    ret_list = []

    for submission in submissions :
        if submission.get_points() >= lowest_passing :
            ret_list.append(submission)  

    return ret_list        


if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)

    for passing in passes:
        print(passing)