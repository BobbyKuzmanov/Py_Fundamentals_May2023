company_names = {}
command = input()
while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in company_names:
        company_names[company] = []
    if employee_id not in company_names[company]:
        company_names[company].append(employee_id)
    command = input()

for company, employee_id in company_names.items():
    print(company)
    for id in employee_id:
        print(f"-- {id}")

# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add
# each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# • Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# • The input always will be valid.
#
# Input:
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
#
# Output:
# SoftUni
# -- AA12345
# -- BB12345
# Microsoft
# -- CC12345
# HP
# -- BB12345

# Input:
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End
#
# Output:
# SoftUni
# -- AA12345
# -- CC12344
# Lenovo
# -- XX23456
# Movement
# -- DD11111
