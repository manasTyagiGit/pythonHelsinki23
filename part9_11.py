class Car :
    def __init__ (self, make: str, top_speed: int) :
        self.make = make
        self.top_speed = top_speed

    
def fastest_car (cars: list) :
    ret_make = cars[0].make
    ret_sped = cars[0].top_speed

    for car in cars :
        if car.top_speed > ret_sped :
            ret_sped = car.top_speed
            ret_make = car.make
    
    return ret_make

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))