def even_numbers_sort(somenumber):
    nums_list = []
    for current in somenumber:
        current_int = int(current)
        if current_int % 2 == 0:
            nums_list.append(current_int)
    return nums_list


user_digit = input().split()
digit = even_numbers_sort(user_digit)
print(digit)

# Description #
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers.
