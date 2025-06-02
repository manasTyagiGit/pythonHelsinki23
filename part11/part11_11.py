from math import *

def square_roots (inp: list) :
    return [sqrt(i) for i in inp]

lines = square_roots([1,2,3,4])
for line in lines:
    print(line)