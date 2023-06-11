wagons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == 'End':
        print(wagons)
        break

    elif command[0] == 'add':
        num_of_people = int(command[1])
        wagons[-1] += num_of_people  # find which wagon is the last one and add the people

    elif command[0] == 'insert':
        index = int(command[1])
        num_of_people = int(command[2])
        wagons[index] += num_of_people

    elif command[0] == 'leave':
        index = int(command[1])
        num_of_people = int(command[2])
        wagons[index] -= num_of_people
