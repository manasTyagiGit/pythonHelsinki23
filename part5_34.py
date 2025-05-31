def find_movies (database : list, search_term : str) : 
    '''
    for dict_obj in database :
        if search_term in dict_obj["name"].lower() :
            print (dict_obj["name"])

    '''
    i = 0
    size = len (database)

    while i < size :
        if search_term in database[i]["name"].lower() :
            print (database[i]["name"])
        i += 1    
    
        
    

def add_movie (database : list, name : str, director : str, year : int, runtime : int) :
    dict_obj = {"name" : name, "director" : director, "year" : year, "runtime" : runtime}

    database.append(dict_obj)

if __name__ == "__main__" :
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)