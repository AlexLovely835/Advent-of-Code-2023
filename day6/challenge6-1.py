with open('day6/challenge6.txt', 'r') as file:
    lines = file.readlines()

times = lines[0].split()[1:]
distances = lines[1].split()[1:]

total_wins = 1

for i in range(0, len(times)):
    win_count = 0
    for j in range(0, int(times[i])):
        if int(distances[i]) <= j * (int(times[i]) - j):
            win_count += 1
    total_wins *= win_count

print("Total ways to win multiplied:", total_wins)