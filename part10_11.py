class Computer :
    def __init__ (self, model: str, speed: int) :
        self.model = model
        self.speed = speed

    def __str__ (self) :
        return f"{self.model}, {self.speed} MHz"

class LaptopComputer (Computer) :
    def __init__ (self, model: str, speed: int, weight: int) :
        super().__init__ (model, speed)
        self.weight = weight
    
    def __str__ (self) :
        init = super().__str__()

        init += f", {self.weight} kg"

        return init


laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)