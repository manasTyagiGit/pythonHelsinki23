def line (a, b) :
    if b == "" :
        b = "*"
    
    print (a * b[0])

def box_of_hashes (a) :
    i = 0
    while i < a :
        line (10, "*")
        i += 1

def square_of_hashes (a) :
    i = 0
    while i < a :
        line (a, "*")
        i += 1
    
def square (a, b) :
    i = 0

    while i < a :
        line (a, b)
        i += 1

def triangle (a) :
    i = 1
    while i <= a :
        line (i, "#")
        i += 1

def triangle (a, b) :
    i = 1
    while i <= a :
        line (i, b)
        i += 1


def shape (a, b, c, d) :
    triangle (a, b)
    i = 1

    while i <= c :
        line (a, d)
        i += 1

def spruce (a) :
    i = 1
    j = 1
    while i <= a :
        space = a - i       
        print (space * " ", end = "")
        print (j * "*")
        i += 1
        j += 2
    
    end_space = a - 1
    print (end_space * " ", end = "*")

def first_word (sen) :
    str = sen.split (" ")
    return str[0]

def second_word (sen) :
    str = sen.split (" ")
    return str[1]

def last_word (sen) :
    str = sen.split (" ")
    return str[len(str) - 1]


if __name__ == "__main__" :
    # box_of_hashes (5)
    # print ()
    # box_of_hashes (7)
    # print ()
    # square_of_hashes (5)
    # print ()
    # square_of_hashes (3)
    # print ()
    # square (3, "o")
    # print ()
    # triangle (3)
    # print ()
    # triangle (6)

    # shape(5, "X", 3, "*")
    # print()
    # shape(2, "o", 4, "+")
    # print()
    # shape(3, ".", 0, ",")

    # spruce (3)
    # print ()
    # spruce (7)

    sentence = "it was a dark and stormy python"
    print (sentence[-1])                # last letter
    print (sentence[-len(sentence)])    # first letter

    print(first_word (sentence)) # it
    print(second_word(sentence)) # was
    print(last_word  (sentence)) # python

    # Trying out depended and independent lists in Python

    orig_list = [1, 2, 3, 4, 5]
    copy_list = orig_list
    inde_list = orig_list[:]

    orig_list[2] = 34

    print (orig_list)
    print (copy_list)
    print (inde_list)




