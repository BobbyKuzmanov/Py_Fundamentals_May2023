my_list = []  # creating a new list where will store input from user
for _ in range(3):
    data = input()
    my_list.append(data)  # adding input from user to our list

my_list[0], my_list[2] = my_list[2], my_list[0]  # swapping values by access them by index
print(my_list)

# head = input()
# body = input()
# tail = input()
# my_list = [tail, body, head]
# my_list[0], my_list[2] = my_list[2], my_list[0]
# print(my_list)

# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# • On the first position is the head;
# • On the second position is the body;
# • On the last one is the tail.
# Input:                             Output:
# my tail                            ['my head is on the wrong end!', 'my body seems on place', 'my tail']
# my body seems on place
# my head is on the wrong end!
