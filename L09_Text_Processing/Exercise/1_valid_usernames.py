usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16:
        if username.isalnum() or "-" in username or "_" in username:
            print(username)

# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
#     • has length between 3 and 16 characters inclusive
#     • can contain only letters, numbers, hyphens, and underscores
#     • has no redundant symbols before, after, or in between
#
# Input:
# sh, too_long_username, !lleg@l ch@rs, jeffbutt
#
# Output:
# jeffbutt