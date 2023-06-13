def find_place_in_lift(people, lift_state):
    lift_state = list(map(int, lift_state.split()))
    total_capacity = len(lift_state) * 4
    remaining_people = people

    for i in range(len(lift_state)):
        while lift_state[i] < 4 and remaining_people > 0:
            lift_state[i] += 1
            remaining_people -= 1

    if remaining_people > 0:
        return f"There isn't enough space! {remaining_people} people in a queue!\n{' '.join(map(str, lift_state))}"
    elif sum(lift_state) < total_capacity:
        return f"The lift has empty spots!\n{' '.join(map(str, lift_state))}"
    else:
        return ' '.join(map(str, lift_state))


# Example usage
people = int(input())
lift_state = input()

result = find_place_in_lift(people, lift_state)
print(result)

# Description #
# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next
# one with space available.
# Input
#   • On the first line, you will receive how many people are waiting to get on the lift
#   • On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
#   When there is no more available space left on the lift, or there are no more people in the queue, you should print
# on the console the final state of the lift's wagons separated by " " and one of the following messages:
# • If there are no more people and the lift have empty spots, you should print:
#   "The lift has empty spots!
#   {wagons separated by ' '}"
# • If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# • If the lift is full and there are no more people in the queue, you should print only the wagons
# separated by " "
# Input: 15
# Output: 0 0 0 0
# Input: 20
# Output: 0 2 0
