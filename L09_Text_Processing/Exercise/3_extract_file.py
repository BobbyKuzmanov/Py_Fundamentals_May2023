path_of_file = input()
file_name = path_of_file.split('\\')[-1]
file_name_without_extension = file_name.split('.')[0]
file_extension = file_name.split('.')[-1]
print(f'File name: {file_name_without_extension}')
print(f'File extension: {file_extension}')

# Write a program that reads the path to a file and subtracts the file name and its extension.
#
# Input:
# C:\Internal\training-internal\Template.pptx
#
# Output:
# File name: Template
# File extension: pptx