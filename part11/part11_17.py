class LotteryNumbers :
    def __init__ (self, week_no: int, lott_arg: list) :
        self.__week_no = week_no
        self.__lott_arg = lott_arg
    
    def number_of_hits (self, numbers: list) :
        return len ([num for num in numbers if num in self.__lott_arg])
    
    def hits_in_place (self, numbers: list) :
        return [num if num in self.__lott_arg else -1 for num in numbers]




week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))
