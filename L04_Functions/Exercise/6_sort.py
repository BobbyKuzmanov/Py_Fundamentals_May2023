def sort_nums(somenumbers):
    my_list = []
    for current in somenumbers:
        my_list.append(int(current))
    sorted_nums = sorted(my_list)
    return sorted_nums

string_nums = input().split()
digits_of_list = sort_nums(string_nums)
print(digits_of_list)

# Description #
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().