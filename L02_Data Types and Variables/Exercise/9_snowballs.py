number_of_snowball = int(input())
max_weight = 0
max_time = 0
max_value = 0
max_quality = 0
for snowball in range(number_of_snowball):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > max_value:
        max_weight = current_weight
        max_time = current_time
        max_value = current_value
        max_quality = current_quality
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")

# Description ### Snowball ###
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# • The weight of the snowball (integer).
# • The time needed for the snowball to get to its target (integer).
# • The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
# • On the first input line, you will receive N – the number of snowballs.
# • On the next N*3 input lines, you will be receiving data about each snowball.
# Output
# • You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
# • The number of snowballs (N) will be an integer in range [0, 100].
# • The weight is an integer in the range [0, 1000].
# • The time is an integer in the range [1, 500].
# • The quality is an integer in the range [0, 100]