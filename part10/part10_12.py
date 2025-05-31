class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year


class GameWarehouse:
    def __init__(self):
        self.games = []

    def add_game(self, game: ComputerGame):
        self.games.append(game)

    def list_games(self):
        return self.games



class GameMuseum (GameWarehouse) :
    def __init__ (self) :
        super().__init__()

    def list_games(self):   
        #self.__games = super().list_games()            # necessary in case of private __games
        ret_list = []

        for game in self.games :
            if game.year <= 1990 :
                ret_list.append (game)

        return ret_list    


museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)