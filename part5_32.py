def histogram (string : str) :
    freq = {}

    for char in string :
        if char not in freq :   # initialize a new char encountered
            freq[char] = 0
        
        freq[char] += 1

    for key in freq :
        print (key, end = " ")
        print (freq[key] * "*")

if __name__ == "__main__" :
    histogram("abba")
    histogram("statistically")