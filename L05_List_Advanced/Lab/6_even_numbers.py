# convert the list of strings into a list of numbers using map function
numbers_list = list(map(int, input().split(', ')))
# Use a map function to iterate over the list to find all the even numbers, and add their indices
found_indices_of_or_no = map(lambda x: x if numbers_list[x] % 2 == 0 else 'no', range(len(numbers_list)))
# Use a map function to iterate over the list to find all the even numbers, and add their indices
even_indices = list(filter(lambda a: a != 'no', found_indices_of_or_no))
print(even_indices)
