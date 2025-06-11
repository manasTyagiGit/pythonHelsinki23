import random

def word_generator(characters: str, length: int, amount: int) :
    for i in range (amount) :
        yield "".join(random.choices (characters, k = length))

        # or yield "".join(characters[randint(0, len(characters) - 1)] for i in range(length))

wordgen = word_generator("abcdefg", 3, 5)
for word in wordgen:
    print(word)