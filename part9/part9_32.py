class Recording :
    def __init__ (self, length: int) :
        self.__length = length

    @property
    def length (self) :
        return self.__length
    
    @length.setter
    def length (self, length: int) :
        if length >= 0 :
            self.__length = length

        else :
            raise ValueError ("Length must be greater than 0 or equal to 0")


the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 54
print(the_wall.length)