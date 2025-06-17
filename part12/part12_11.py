def order_by_stock (inp: tuple) :
    return inp[2]

def sort_by_remaining_stock (products: list) :
    products.sort(key = order_by_stock, reverse = True)
    return products

    # return sorted (products, key = order_by_sorted)

products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")