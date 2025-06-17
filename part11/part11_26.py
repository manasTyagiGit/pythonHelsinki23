def most_common_words(filename: str, lower_limit: int) :
    file_handler = open (filename, "r")   

    freq = {}

    for line in file_handler :
        words = line.split(" ")
        for word in words :
            if word not in freq :
                freq[word] = 1
            else :
                freq[word] += 1

    ret_dict = {x : freq[x] for x in freq if freq[x] >= lower_limit}

    return ret_dict  


if __name__ == "__main__" :
    filename = "/home/manas_tyagi/Data/Programming/Python/part11/comprehensions.txt"
    print ("Hello")
    print (most_common_words (filename, 2))