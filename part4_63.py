def longest_series_of_neighbours (list : list) -> int :    
    max_count = 0
    
    i = 1
    size = len (list) - 1
    
    count = 0

    while i <= size :
        if list[i] - list[i - 1] == 1 or list[i] - list[i - 1] == -1 :
            count += 1
        else :
            count = 0
        
        #print ("count:", count)

        if count > max_count :
            max_count = count
        i += 1

    return max_count + 1


if __name__ == "__main__" :
    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))