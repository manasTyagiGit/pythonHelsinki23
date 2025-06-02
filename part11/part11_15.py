def remove_smaller_than (nums: list, key: int) :
    return [n for n in nums if n >= key]

numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))