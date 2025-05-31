my_list = []

word = input ("Word: ")
my_list.append (word)
i = 1

while True :
    wordnew = input ("Word: ")
    if wordnew in my_list :
        break
    else :
        my_list.append (wordnew)
        i += 1


print (i)

