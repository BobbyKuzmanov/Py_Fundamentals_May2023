next_pair_row = int(input())
students_grades = {}
for _ in range(next_pair_row):
    student_name = input()
    grade = float(input())
    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(grade)

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")


# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to
# 4.50.
# Print the final dictionary with students and their average grade in the following format:
#   "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
#
# Input:
#   5
#   John
#   5.5
#   John
#   4.5
#   Alice
#   6
#   Alice
#   3
#   George
#   5
#
# Output:
#   John -> 5.50
#   Alice -> 4.50
#   George -> 5.00
