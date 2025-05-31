from random import sample

def lottery_numbers (size: int, low: int, high: int) -> list :
    number_pool = list(range(low, high + 1))
    nums = sample(number_pool, size)

    retList = sorted(nums)

    return retList

for number in lottery_numbers(7, 1, 40):
    print(number)