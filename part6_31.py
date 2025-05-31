def new_person (name: str, age: int) -> tuple :
    return (name, age)

if __name__ == "__main__" :
    
    name = input ("Enter your full name : ")
    if len(name) == 0 :
        raise ValueError ("Name cannot be empty")      
    
    elif len(name) > 40 :
        raise ValueError ("Name is too long")
    
    elif name :
        sent = name.split (" ")
        print (f"sent == {sent}")

        if len(sent[0]) == 0 :
            raise ValueError ("Error, must have two words")

        elif len (sent[1]) == 0 :
            raise ValueError ("Error, must have two words")
        
        # try :
        #     if len(sent[1]) == 0 :
        #         raise ValueError ("Error, must have two words")
        # except IndexError :
        #         raise ValueError ("Error, must have two words")

    
    age = int (input ("Enter your age : "))
    
    if age < 0 :
        raise ValueError ("Age cannot be negative")
    
    elif age > 150 :
        raise ValueError ("Age cannot be greater than 150")    
   
    
    new_person (name, age)
    print (new_person(name, age))
    