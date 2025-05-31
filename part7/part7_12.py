import string

def separate_characters (inpStr : str) :
    ascii = ""
    punct = ""
    other = ""

    for letter in inpStr :
        if letter in string.ascii_letters :
            ascii += letter
        elif letter in string.punctuation :
            punct += letter
        else :
            other += letter
    
    return [ascii, punct, other]


parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])