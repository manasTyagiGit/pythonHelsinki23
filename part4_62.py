def most_common_character (string : str) -> str :
    freq = [0] * 26         # freq = range (100) -> to create a list from 0 to 99
    
    string = string.lower()
    
    size = len(string) - 1
    i = 0

    while i <= size :
        index = ord(string[i]) - 97
        freq[index] += 1
        i += 1   

    index = freq.index (max(freq))    
    max_char = chr (97 + index)

    # may use the below snippet for line 14-15
    '''
    i = 1
    while i <= 25 :
        if freq[i] > freq[ord(max_char) - 97] :
            max_char = chr (97 + i)
        i += 1 
    '''

    return max_char 


if __name__ == "__main__" :
    first_string = "abcdbde"
    print(most_common_character(first_string))
    

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))