def fill_shells(num_electrons):
    shells = []
    shell_number = 1

    while num_electrons > 0:
        max_electrons = 2 * shell_number ** 2

        if num_electrons >= max_electrons:
            shells.append(max_electrons)
            num_electrons -= max_electrons
        else:
            shells.append(num_electrons)
            num_electrons = 0

        shell_number += 1

    return shells


# Prompt the user for the number of electrons
num_electrons = int(input())

# Fill the shells and print the result
filled_shells = fill_shells(num_electrons)
print(filled_shells)
