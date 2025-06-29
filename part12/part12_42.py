import json

def print_set (inp_set) :
    for item in inp_set :
        print (item)

def print_player (player) :
    name = player["name"]
    team = player["team"]
    goals = player["goals"]
    assists = player["assists"]
    points = goals + assists

    print(f"{name:21s}{team:5s}{goals:2d} + {assists:2d} = {points:3d}")

def player_search (json_data) :
    name = input ("name: ")

    for player in json_data :
        if (player["name"] ==  name) :
            print_player(player)
            return
        
    print ("Not found")


def list_teams (json_data) :

    team_set = set()

    for player in json_data :
        team_set.add(player["team"])

    return sorted (team_set)


def list_countries (json_data) :
    country_set = set()

    for player in json_data :
        country_set.add (player["nationality"])

    return sorted(country_set)

def player_in_team (json_data, team) :
    player_list = []

    for player in json_data :
        if player["team"] == team :
            player_list.append(player)

    player_list = sorted (player_list, key = lambda x : x["goals"] + x["assists"], reverse = True)

    for player in player_list :
        print_player(player)

def player_in_country (json_data, country) :
    player_list = []

    for player in json_data :
        if player["nationality"] == country :
            player_list.append (player)

    player_list = sorted (player_list, key = lambda x : x["goals"] + x["assists"], reverse = True)

    for player in player_list :
        print_player (player)

def top_points_players (json_data, final) :
    player_list = []

    for player in json_data :
        player_list.append(player)

    player_list = sorted (player_list, key = lambda x : (x["goals"] + x["assists"], x["goals"]), reverse = True)

    player_list = player_list[:final]

    for player in player_list :
        print_player(player)

def top_goals_players (json_data, final) :

    player_list = []

    for player in json_data :
        player_list.append(player)

    player_list = sorted (player_list, key = lambda x : (x["goals"], -x["goals"]), reverse = True)

    player_list = player_list[:final]

    for player in player_list :
        print_player(player)


if __name__ == "__main__" :
    file = input("File name: ")    

    try :
        file_handle = open (file, "r")
        json_data = json.load(file_handle)    
    
    except FileNotFoundError:
        print ("File does not exist, quitting")
        exit(-1)

    print ("commands:\n0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country")
    print ("6 most points\n7 most goals")

    while True :
        choice = int(input("command: "))

        if choice == 0 :
            exit(0)

        elif choice == 1 :
            player_search (json_data)

        elif choice == 2 :
            teams = list_teams (json_data)

            print_set (teams)

        elif choice == 3:
            countries = list_countries (json_data)

            print_set (countries)

        elif choice == 4:
            team = input ("Team: ")
            player_in_team (json_data, team)
        
        elif choice == 5:
            country = input ("Country: ")
            player_in_country (json_data, country)

        elif choice == 6:
            final = int(input("How many? : "))
            top_points_players (json_data, final)

        elif choice == 7:
            final = int (input("How many? : "))
            top_goals_players (json_data, final)

        else :
            print ("Wrong choice, quitting")
            exit(-1)
