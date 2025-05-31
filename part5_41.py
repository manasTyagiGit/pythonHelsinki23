def create_tuple (x :int, y :int, z :int) :
    init_list = []
    init_list.append (x)
    init_list.append (y)
    init_list.append (z)

    ret_tuple = ()                    # or use a list, append to it and then typecast

    ret_tuple += (min (init_list),)
    ret_tuple += (max (init_list),)

    ret_tuple += (sum (init_list),)  

    ret_tuple += ("Hey nonhomo", )    # tuples can store non-homogenous data


    return ret_tuple

if __name__ == "__main__" :
    print(create_tuple(5, 3, -1))