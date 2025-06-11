def prime_numbers () :
    num = 2

    while True :
        prime = True
        for i in range (2, num) :
            if num % i == 0 :
                prime = False
                break
        
        if prime :
            yield num
        
        num += 1


numbers = prime_numbers()
for i in range(8):
    print(next(numbers))