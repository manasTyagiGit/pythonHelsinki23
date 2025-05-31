class Car :
    def __init__ (self) :
        self.__fuel = 0
        self.__odo  = 0
    
    def __str__ (self) :
        return f"Car: odometer reading {self.__odo} km, petrol remaining {self.__fuel} litres"
    
    def fill_up (self) :
        self.__fuel = 60

    def drive (self, km: str) :
        if km > self.__fuel :
            self.__odo += self.__fuel
            self.__fuel = 0

        else :
            self.__odo += km
            self.__fuel -= km


car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)