participant_submissions = {}
participant_points = {}
banned_participants = []

while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")
    username = command[0]
    language = command[1]
    points = int(command[2])
    if username == "banned":
        banned_participants.append(username)
        continue
    if language not in participant_submissions:
        participant_submissions[language] = 0
    participant_submissions[language] += 1
    if username not in participant_points:
        participant_points[username] = 0
    if points > participant_points[username]:
        participant_points[username] = points

for participant in participant_points:
    if participant in banned_participants:
        participant_points.pop(participant)

print("Results:")
for participant in participant_points:
    print(f"{participant} | {participant_points[participant]}")

print("Submissions:")
for language in participant_submissions:
    print(f"{language} - {participant_submissions[language]}")

# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive
# "exam finished". You should store each username and their submissions and points. If a student has two or
# more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that
# case, you should remove the user from the contest but preserve his submissions in the total count of submissions
# for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
# "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# • Print the exam results for each participant
# • After that, print each language in the format shown above
# • Allowed working time / memory: 100ms / 16MB
#
# Input:
# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished
#
# Output:
# Results:
# Peter | 84
# George | 84
# Katy | 94
# Submissions:
# Java - 1
# C# - 3
#
# Input:
# Peter-Java-91
# George-C#-84
# Katy-Java-90
# Katy-C#-50
# Katy-banned
# exam finished
#
# Output:
# Results:
# Peter | 91
# George | 84
# Submissions:
# Java - 2
# C# - 2
