class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    @property
    def euros (self) :
        return self.__euros
    
    @property
    def cents (self) :
        return self.__cents
    
    def __eq__(self, another) :

        # if self.euros != another.euros  :   return False
        # if self.cents != another.cents  :   return False

        return (self.euros == another.euros) and (self.cents == another.cents)  

    def __ne__ (self, another) :
        return (self.euros != another.euros) or  (self.cents != another.cents)

    def __lt__(self, another):
        if self.euros < another.euros   :       return True

        if self.euros == another.euros  :
            if self.cents < another.cents   :   return True

        return False 

    def __gt__(self, another) :
        return not self.__lt__(another)         # not really true, but you get the point


    def __add__(self, another) :
        cents = self.cents + another.cents
        euros = self.euros + another.euros

        if cents >= 100 :
            euros += cents // 100
            cents %= 100

        return Money (euros, cents)
    
    def __sub__ (self, another) :
        actual_cents_self = self.euros * 100 + self.cents
        actual_cents_another = another.euros * 100 + another.cents

        diff = actual_cents_self - actual_cents_another

        if diff < 0 :
            raise ValueError ("Cannot be negative")
        
        else :
            euros = diff // 100
            cents = diff % 100
            return Money(euros, cents)


    
e1 = Money(4, 5)
print(e1)
e1.euros = 1000
print(e1)