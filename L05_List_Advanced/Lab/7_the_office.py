# read the input
employees = input().split(" ")
happiness_factor = int(input())
# use the map() function to multiply each element with the factor
employees = list(map(lambda x: int(x) * happiness_factor, employees))
# filter the elements that are greater than the average
filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
# print the result
if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are not happy!')

# def check_employee_happiness():
#     happiness_list = list(map(int, input().split(' ')))
#     happiness_factor = int(input())
#
#     improve_happiness = [h * happiness_factor for h in happiness_list]
#
#     average_happiness = sum(improve_happiness) / len(improve_happiness)
#     happy_count = sum(h >= average_happiness for h in improve_happiness)
#     total_count = len(improve_happiness)
#
#     message = 'happy' if happy_count >= total_count / 2 else 'not happy'
#     result = f"Score: {happy_count}/{total_count}. Employees are {message}!"
#
#     return result
#
#
# result = check_emplayee_happiness()
# print(result)
