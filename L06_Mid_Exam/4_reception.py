def time_needed(employee1, employee2, employee3, students_count) -> __name__:
    total_efficiency = employee1 + employee2 + employee3
    time = 0

    while students_count > 0:
        time += 1
        if time % 4 != 0:
            students_count -= total_efficiency

    return time


if __name__ == "__main__":
    employee1 = int(input())
    employee2 = int(input())
    employee3 = int(input())
    students_count = int(input())

    time = time_needed(employee1, employee2, employee3, students_count)
    print(f"Time needed: {time}h.")

# Description #
# Three employees are working on the reception all day. Each of them can handle a different number of students per
# hour. Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers, representing the number of students that each employee can help per
# hour. On the following line, you will receive students count as a single integer.
# Every fourth hour, all employees have a break, so they don't work for an hour. It is the only break for the
# employees, because they don't need rest, nor have a personal life. Calculate the time needed to answer all the
# student's questions and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# • On the first three lines - each employee efficiency - integer in the range [1 - 100]
# • On the fourth line - students count – integer in the range [0 – 10000]
# • Input will always be valid and in the range specified
# Output
# • Print a single line: "Time needed: {time}h."
# • Allowed working time / memory: 100ms / 16MB
