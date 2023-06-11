user_input = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = ''.join([letter for letter in user_input if letter not in vowels])
print(no_vowels)

# text = input()
# sorted_text = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
# print(''.join(sorted_text))
# Description # Using comprehension, write a program that receives a text and removes all its vowels,
# case_insensitive.
# Print the new text string after removing the vowels.
# The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
