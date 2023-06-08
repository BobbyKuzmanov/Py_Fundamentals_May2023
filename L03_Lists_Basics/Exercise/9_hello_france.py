items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150
for item in items:
    type, buying_price = item.split("->")
    buying_price = float(buying_price)
    price_is_valid = False
    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            sell_prices.append(sell_price)

for sell_price in sell_prices:
    print(f"{sell_price:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

# Description #
# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you
# decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type Maximum Price
# Clothes 50.00
# Shoes 35.00
# Accessories 20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have
# to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items
# as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if
# the budget after selling all the items is enough for buying the train ticket.
# Input / Constraints
# • On the 1st line, you will receive the items with their prices in the format described above – real numbers in the
# range [0.00……1000.00]
# • On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
# • First, print the list with the bought item’s new prices, formatted to the second decimal point in the following
# format:
# "{price1} {price2} {price3} … {priceN}"
# Input Output
# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
# 220
# Cells:
# - 40
# - 110
# Effort: 37.50
# Total Fire:
# 150© SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 7 of 9
# • Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# • Finally:
# o If the budget is enough for buying the train ticket, print: "Hello, France!"
# o Otherwise, print: "Not enough money."
