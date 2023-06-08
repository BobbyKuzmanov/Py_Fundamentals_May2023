divasor_num = int(input())
boundary = int(input())

for number in range(boundary,divasor_num - 1, -1):
    if number % divasor_num == 0:
        break

print(number)
