def oldest_person (people :list) :
    size_of_list = len (people)

    i = 0
    min_year = 2000
    index = 0

    while i < size_of_list :
        if people[i][1] < min_year :
            min_year = people[i][1]
            index = i
        i += 1

    return people[index][0]

if __name__ == "__main__" :
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))