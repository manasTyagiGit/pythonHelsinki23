class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.products):
            product = self.products[self.i]
            self.i += 1
            return product
        else:
            raise StopIteration

def products_in_shopping_list(shopping_list: list, amount: int) :
    return [item[0] for item in shopping_list if item[1] >= amount]


my_list = ShoppingList()
my_list.add("bananas", 10)
my_list.add("apples", 5)
my_list.add("alcohol free beer", 24)
my_list.add("pineapple", 1)

print("the shopping list contains at least 5 of the following items:")
for product in products_in_shopping_list(my_list, 5):
    print(product)