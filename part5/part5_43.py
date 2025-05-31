def older_people (people :list, year :int) :
    list_older = []

    for person in people :
        if person[1] < year :
            list_older.append (person[0])

    return list_older

if __name__ == "__main__" :
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1979)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)