def even_numbers (beginning: int, maximum: int) :
    num = beginning

    if num % 2 != 0 :   num += 1

    while num <= maximum :
        yield num
        num += 2

numbers = even_numbers(11, 21)
for number in numbers:
    print(number)