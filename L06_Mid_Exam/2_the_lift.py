people_waiting = int(input())
lift_state = list(map(int, input().split()))

total_wagons = len(lift_state)
current_wagon = 0

while people_waiting > 0 and current_wagon < total_wagons:
    available_space = 4 - lift_state[current_wagon]
    if available_space >= people_waiting:
        lift_state[current_wagon] += people_waiting
        people_waiting = 0
    else:
        lift_state[current_wagon] += available_space
        people_waiting -= available_space
    current_wagon += 1

if people_waiting == 0 and 0 in lift_state:
    print("The lift has empty spots!")
    print(" ".join(map(str, lift_state)))
elif people_waiting > 0 and current_wagon == total_wagons:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(map(str, lift_state)))
else:
    print(" ".join(map(str, lift_state)))
