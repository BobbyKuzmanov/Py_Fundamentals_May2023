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

 # Description #
# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. Until you receive the command "End", you will receive some of the following commands:
#     • "add {people}" – you should add the number of people in the last wagon
#     • "insert {index} {people}" - you should add the number of people at the given wagon
#     • "leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.
