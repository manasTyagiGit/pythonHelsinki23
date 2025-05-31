def everything_reversed (my_list : list) -> list :

    ret_list = my_list
    i = 0
    size = len (ret_list)       
    #print (size) 

    for i in range (0, size) :            # analogous to for i in [0, size - 1]
        #print (i, end = " ")
        ret_list[i] = ret_list[i][::-1]            
        
    return ret_list[::-1]


if __name__ == "__main__" :
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed (my_list)
    print (new_list)