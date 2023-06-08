product = input()
quantity = int(input())


def calculate_price(item, num_of_items):
    if item == 'coffee':
        price = 1.50
    elif item == 'coke':
        price = 1.40
    elif item == 'water':
        price = 1.00
    elif item == 'snacks':
        price = 2.00
    return f'{price * num_of_items:.2f}'


print(calculate_price(product, quantity))

# Description
# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
#  • coffee - 1.50
#  • water - 1.00
#  • coke - 1.40
#  • snacks - 2.00
# Print the result formatted to the second decimal place.
