def invert (s : dict) :
    temp = {}

    for key, value in s.items() :
        temp[value] = key        
    
    s.clear()

    for key, value in temp.items() :
        s[key] = value
   
        
if __name__ == "__main__" :

    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)