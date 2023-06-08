number_of_messages = int(input())

for current_message in range(number_of_messages):
    codes = int(input())
    if codes == 88:
        message = "Hello"
    elif codes == 86:
        message = "How are you?"
    elif codes < 88:
        message = "GREAT!"
    else:  # codes > 88
        message = 'Bye.'

    print(message)
