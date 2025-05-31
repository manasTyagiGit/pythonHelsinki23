class Person :
    
    def __init__ (self, name: str) :
        self.first_name = name.split(" ")[0]
        self.last_name  = name.split(" ")[1]

    def return_first_name(self) :
        return self.first_name
    
    def return_last_name(self) :
        return self.last_name
        

if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())