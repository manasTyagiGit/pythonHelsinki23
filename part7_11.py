from math import *

def hypotenuse (x: int, y: int) -> float :
    z = sqrt ((x*x) + (y*y))

    return z

# 5.0
# 13.0
# 1.4142135623730951


print(hypotenuse(3,4)) # 5.0
print(hypotenuse(5,12)) # 13.0
print(hypotenuse(1,1)) # 1.4142135623730951