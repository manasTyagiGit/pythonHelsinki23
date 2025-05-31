class Series :

    def __init__ (self, name: str, seasons: int, genre: list) :
        self.name = name
        self.seasons = seasons
        self.genre = genre
        self.ratings = 0
        self.sum_of_ratings = 0

    def __str__ (self) :
        genre_string = ",".join(self.genre)
        
        return (
            f"{self.name} ({self.seasons} Seasons)\n"
            f"genres: {genre_string}\n"
            f"{self.ratings} ratings, average {self.sum_of_ratings / self.ratings:.1f} rating"
        )
    
    def rate (self, rating: int) :
        self.ratings += 1
        self.sum_of_ratings += rating


def minimum_grade(rating: float, series_list: list) :
    ret_list = []

    for series in series_list :
        if series.sum_of_ratings / series.ratings >= rating :
            ret_list.append(series)

    return ret_list

def includes_genre (genre: str, series_list) :
    ret_list = []

    for series in series_list :
        if series.genre.count (genre) >= 1 :
            ret_list.append (series)

    return ret_list


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.name)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.name)