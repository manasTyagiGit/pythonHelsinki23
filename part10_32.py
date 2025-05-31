class ShoppingList :
    def __init__ (self) :
        self._items = []        

    def add (self, item_name: str, item_quantity: int) :        
        self._items.append((item_name, item_quantity))

    def __iter__(self) :
        self.n = 0
        return self
    
    def __next__ (self) :
        sz = len(self._items)

        if self.n < sz :
            cur_item = self._items[self.n]

            self.n += 1
            return cur_item
        
        else :
            raise StopIteration


if __name__ == "__main__" :
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")