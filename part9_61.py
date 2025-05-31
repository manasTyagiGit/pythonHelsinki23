class Item :
    def __init__ (self, name: str, weight: int) :
        self.__name = name
        self.__weight = weight

    def __str__ (self) :
        return f"{self.__name} ({self.__weight} kg)"    
    
    def name (self) :
        return self.__name    
    
    def weight (self) :
        return self.__weight
    
class Suitcase :
    def __init__ (self, max_weight: int) :
        self.max_weight = max_weight
        self.item_list = []   
    
    def __calc_cur_weight(self)  :
        cur_weight = 0
        for itm in self.item_list :
            cur_weight += itm.weight()

        return cur_weight

    def add_item (self, item: "Item") :
        cur_weight = self.__calc_cur_weight()        

        if cur_weight + item.weight() <= self.max_weight :
            self.item_list.append (item)            

        else :
            print ("Item cannot be added as it exceeds available weight limit")

    def __str__ (self) :
        cur_weight = self.__calc_cur_weight()

        if len(self.item_list) == 1:
            return f"1 item, ({cur_weight} kg)"
        
        return f"{len(self.item_list)} items, ({cur_weight} kg)"
    
    def weight (self) :
        cur_weight = self.__calc_cur_weight()

        return cur_weight
    
    def print_items (self) :
        for item in self.item_list :
            print (item)

    def heaviest_item (self) :
        if len (self.item_list) == 0 :
            return None
        
        heaviest = self.item_list[0]

        for item in self.item_list :
            if item.weight() > heaviest.weight() :
                heaviest = item

        return item
    
class CargoHold :
    def __init__ (self, max_weight: int) :
        self.max_weight = max_weight
        self.suit_list = []    

    def add_suitcase (self, suitcase: "Suitcase") :
        cur_weight = 0

        for suit in self.suit_list :
            cur_weight += suit.weight()        

        if cur_weight + suitcase.weight() <= self.max_weight :
            self.suit_list.append(suitcase)
        
        else :
            print ("Suitcase exceeds current limit of the cargo\n")

    def __str__(self) :
        cur_weight = 0

        for suit in self.suit_list :
            cur_weight += suit.weight()
        
        left_over = self.max_weight - cur_weight

        return f"{len(self.suit_list)} suitcases, space for {left_over} kg"
    
    def print_items (self) :
        for suit in self.suit_list :
            suit.print_items()


######### test code ####################

book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()