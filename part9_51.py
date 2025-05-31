class ListHelper :  

    @classmethod
    def calc_freq (cls, numbers: list) :

        freq = {}

        for number in numbers :
            if number in freq :
                freq[number] += 1
            else :
                freq[number] = 1 

        return freq 
        

    @classmethod
    def greatest_frequency (cls, numbers: list) :
        freq = ListHelper.calc_freq (numbers)

        max_freq_key = 0
        max_freq = 0

        for key in freq :
            if freq[key] > max_freq :
                max_freq_key = key
                max_freq = freq[key]

        return max_freq_key
    
    @classmethod
    def doubles (cls, numbers: list) :

        freq = ListHelper.calc_freq (numbers)

        double_list = []

        for key in freq :
            if freq[key] >= 2 :
                double_list.append(key)

        return (len (double_list))



numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))