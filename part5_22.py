def remove_smallest (num_list : list) -> list :
    num_list.remove(min(num_list))

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)