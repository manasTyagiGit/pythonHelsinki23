def total_result (person: dict) -> int :
    total = 0

    for key, value in person.items() :
        if key == "name" :
            continue
        total += value 
    
    return total

def smallest_average(person1: dict, person2: dict, person3: dict) -> dict :
    sum1 = total_result (person1) 
    sum2 = total_result (person2) 
    sum3 = total_result (person3)

    if sum1 < sum2 and sum1 < sum3 : 
        return person1
    elif sum2 < sum1 and sum2 < sum3 :
        return person2
    else :
        return person3   


if __name__ == "__main__" :
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))