def solve(a, b, operator: str):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    else:
        result = 'Error: Unknown operator '
    return result


operator = input()
first_num = int(input())
second_num = int(input())

print(solve(first_num, second_num, operator))

# Description #
# Create a function that receives three parameters, calculates a result depending on the given operator, and returns
# it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one
# of the following: "multiply", "divide", "add", "subtract".
