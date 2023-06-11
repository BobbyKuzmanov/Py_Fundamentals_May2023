names = input().split(', ')

sorted_list = sorted(names, key=lambda x: (-len(x), x))

print(sorted_list)

# def sort_names():
#     names_list = input().split()
#     sorted_names = sorted(names_list, key=lambda x: (-len(x), x))
#
#
# result = sort_names()
# print(result)
