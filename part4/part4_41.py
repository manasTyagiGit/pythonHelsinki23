def formatted (my_list : list) -> list :
    fmt_list = []

    for i in my_list :
        fmt_list.append (f"{i:.2f}")

    return fmt_list


if __name__ == "__main__" :
    my_list = [1.234, 0.3333, .11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)