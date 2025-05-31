class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0               

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum (self) :
        return self.sum
    
    def average (self) :
        if self.numbers > 0:
            return self.sum / self.numbers
        
        return 0;

if __name__ == "__main__" :    
    stats = NumberStats ()
    stats_even = NumberStats ()
    stats_odd = NumberStats ()

    print ("Please type in integer numbers:")

    while True:
        inp = int(input())

        if (inp == -1) :    break

        stats.add_number(inp)  

        # call EVEN
        if inp % 2 == 0 :
            stats_even.add_number(inp)
        #call ODD
        else :
            stats_odd.add_number(inp)

    
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", stats_even.get_sum())
    print("Sum of odd numbers", stats_odd.get_sum())