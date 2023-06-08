number = int(input())

for first_sign in range(number):
    for second_sign in range(number):
        for third_sign in range(number):
            print(f'{chr(97 + first_sign)}{chr(97 + second_sign)}{chr(97 + third_sign)}')
# Description ### Triple_latin_letters ###
# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically.
