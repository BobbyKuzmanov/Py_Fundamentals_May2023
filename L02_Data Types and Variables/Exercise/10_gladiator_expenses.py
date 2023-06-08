lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_lost_helmets = lost_fight_count // 2  # with modular we found how many times lost fight
total_lost_swords = lost_fight_count // 3
total_lost_shields = lost_fight_count // (2 * 3)
total_lost_armor = total_lost_shields // 2
total_cost = total_lost_helmets * helmet_price \
             + total_lost_swords * sword_price \
             + total_lost_shields * shield_price \
             + total_lost_armor * armor_price
print(f"Gladiator expenses: {total_cost:.2f} aureus")

# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a
# helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his
# equipment.
# Input / Constraints
# The input will consist of 5 lines:
# • On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# • On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# • On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# • On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# • On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# Output
# • As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses:{expenses} aureus"
