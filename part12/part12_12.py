def order_by_seasons (inp: dict) :
    return inp["seasons"]

def order_by_ratings (inp: dict) :
    return inp["rating"]

def sort_by_seasons (shows: list) :
    return sorted (shows, key = order_by_seasons)

def sort_by_ratings (shows: list) :
    return sorted (shows, key = order_by_ratings, reverse = True)


shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, 
         { "name": "Friends", "rating" : 8.9, "seasons":10 },  
         { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")

print("Rating according to IMDB")
for show in sort_by_ratings(shows):
    print(f"{show['name']}  {show['rating']}")