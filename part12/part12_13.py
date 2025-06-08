class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"
    
class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"
    

def order_by_length (obj : ClimbingRoute) :
    return obj.length

def order_by_difficulty (obj: ClimbingRoute) :
    return obj.grade

def sort_by_length (routes: list) :
    return sorted (routes, key = order_by_length, reverse = True)

def sort_by_difficulty (routes: list) :
    return sorted (routes, key = order_by_difficulty, reverse = True)

def order_by_no_of_routes (obj: ClimbingArea) :
    return obj.routes()

def sort_by_number_of_routes (areas: list) :
    return sorted (areas, key = order_by_no_of_routes)

def order_by_hardest (obj: ClimbingArea) :
    return obj.hardest_route().grade

def sort_by_most_difficult (areas: list) :
    return sorted (areas, key = order_by_hardest, reverse = True)
    


## TEST ##

ca1 = ClimbingArea("Olhava")
ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

ca2 = ClimbingArea("Nummi")
ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

ca3 = ClimbingArea("Nalkkila slab")
ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

areas = [ca1, ca2, ca3]
for area in sort_by_most_difficult(areas):
    print(area)