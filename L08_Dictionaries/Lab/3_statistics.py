products = {}

command = input()
while command != "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity

    command = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")


# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command
# "statistics". Sometimes you may receive a product more than once. In that case, you have to add the new
# quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"
#
# Input:
#
# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics
#
# Output:
# #
# Products in stock:
# - bread: 5
# - cheese: 2
# - ham: 1
# Total Products: 3
# Total Quantity: 8
#
# Input:

# eggs: 10
# bread: 6
# cheese: 8
# milk: 7
#
# Output:

# Products in stock:
# - eggs: 10
# - bread: 6
# - cheese: 8
# - milk: 7
# Total Products: 4
# Total Quantity: 31