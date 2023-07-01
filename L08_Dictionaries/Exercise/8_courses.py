lines = input().split(" : ")
courses = {}
while not lines[0] == "end":
    if lines[0] not in courses:
        courses[lines[0]] = []
    courses[lines[0]].append(lines[1])
    lines = input().split(" : ")

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")

# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each
# course, print the registered users.
# Input
#   • Until the "end" command is received, you will be receiving input lines in the format:
#   "{course_name} : {student_name}"
#   • The product data is always delimited by " : "
# Output
#   • Print the information about each course in the following format:
#   "{course_name}: {registered_students}"
#   • Print the information about each student in the following format:
#   "-- {student_name}"
#
# Input:
#   Programming Fundamentals : John Smith
#   Programming Fundamentals : Linda Johnson
#   JS Core : Will Wilson
#   Java Advanced : Harrison White
#   end
#
# Output:
#   Programming Fundamentals: 2
#   -- John Smith
#   -- Linda Johnson
#   JS Core: 1
#   -- Will Wilson
#   Java Advanced: 1
#   -- Harrison White
