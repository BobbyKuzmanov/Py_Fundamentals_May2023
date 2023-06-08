number_of_lines = int(input())
tank_capacity = 255
water_count = 0

for current_level in range(number_of_lines):
    litres_of_water = int(input())
    if tank_capacity - litres_of_water < 0:  # If not enough capacity
        print("Insufficient capacity!")
        continue
    tank_capacity -= litres_of_water
    water_count += litres_of_water
print(water_count)

# Description ### Water overflow ###
# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last
# line, print the liters in the tank