def times_ten (a : int, b : int) -> dict :
    ret_dict = {}
    i = a

    while i <= b :
        ret_dict[i] = i * 10
        i += 1

    return ret_dict

if __name__ == "__main__" :
    d = times_ten(3, 6)
    print(d)