def add_numbers_to_list(numbers: list) :    
    if len(numbers) % 5 == 0 :  return      # base condition

    last = numbers[-1]
    numbers.append(last + 1)

    add_numbers_to_list (numbers)

numbers = [1,3,4,5,10,11,13]
add_numbers_to_list(numbers)
print(numbers)