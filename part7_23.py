import random

def words (size: int, begin: str) :
    file = open ("word.txt", 'r')

    inputList = []

    for word in file :
        word = word.replace ("\n", "")
        if word.startswith(begin) :
            inputList.append (word)

    # print (inputList)

    sizeInput = len(inputList)

    outputList = []

    if sizeInput < size :
        raise ValueError (f"Not enough words start with {begin} in our file")

    for i in range(size) :
        indexRandom = random.randint (0, sizeInput - 1)
        wrd = outputList.append(inputList[indexRandom])
    

    return outputList

##############################################################

word_list = words(3, "ca")

for word in word_list:
    print(word)