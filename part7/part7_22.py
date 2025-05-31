import random
import string

def generate_strong_password (leng: int, includeNum: bool, includeSpcl: bool) -> str :

    inputLetters = string.ascii_letters

    if includeNum :
        inputLetters += '0123456789'

    if includeSpcl :
        inputLetters += '!?=+-()#'

    size = len (inputLetters) - 1
    pwd= ""

    for i in range (leng) :
        index_random = random.randint(0, size)
        pwd = pwd + inputLetters[index_random]

    return pwd


for i in range(5):
    print(generate_strong_password(22, True, True))