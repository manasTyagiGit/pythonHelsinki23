my_list = []

print ("The list is now", my_list)
op = input ("a(d)d, (r)emove or e(x)it: ")
i = 0

while op != "x" :
    if op == "d" :
        i += 1
        my_list.append (i)        
    
    elif op == "r" :
        if len(my_list) == 0 :
            print ("List is empty")
            break
        
        my_list.remove (i)
        i -= 1

    print ("The list is now", my_list)
    op = input ("a(d)d, (r)emove or e(x)it: ")



