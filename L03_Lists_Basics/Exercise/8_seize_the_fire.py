cells = input().split("#")
amount_of_water = int(input())
total_fire = 0
total_effort = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
for cell in cells:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False
    if type_of_fire == "High":
        if cell_value in high:
            cell_is_valid = True
    elif type_of_fire == "Medium":
        if cell_value in medium:
            cell_is_valid = True
    elif type_of_fire == "Low":  # else:
        if cell_value in low:
            cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            fire_out_cells.append(cell_value)
            total_fire += cell_value
            total_effort += cell_value * 0.25
print("Cells:")
for fire_out_cell in fire_out_cells:
    print(f"- {fire_out_cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

# Description #
# Create a program that calculates the water needed to put out a "fire cell", based on the given information about its
# "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed
# water to put out the fire. They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} =
# {valueOfCell}"© SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 5 of 9
# Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each
# fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire Range
# High 81 - 125
# Medium 51 - 80
# Low 1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort, and you
# need to calculate it. Its value is equal to 25% of the cell's value. In the end, you will have to print the total effort. Keep
# putting out cells until you run out of water. Skip it and try the next one if you do not have enough water to put out a
# given cell. In the end, print the cells you have put out in the following format:
# "Cells:
# - {cell1}
# - {cell2}
# … -
# {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"
# Input / Constraints
# • On the 1st line, you will receive the fires with their cells in the format described above – integer numbers in the
# range [1…500].
# • On the 2nd line, you will receive the water – an integer number in the range [0….100000].
# Output
# Print the output as described above.
