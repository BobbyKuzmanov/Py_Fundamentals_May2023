def loading_bar(some_number):
    if some_number == 100:
        return f'{some_number}% Complete! \n[%%%%%%%%%%]'
    loaded_percent = some_number // 10
    return f"{some_number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))

#Description#
# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20,
# 30...). Your task is to create a function that returns a loading bar depending on the number you have received in the
# input. Print the result on the console. For more clarification, see the examples below.
# Examples
# Input       Output
# 30        30% [%%%.......]
#           Still loading...
# 50        50% [%%%%%.....]
#           Still loading...
# 100       100% Complete!
#           [%%%%%%%%%%]