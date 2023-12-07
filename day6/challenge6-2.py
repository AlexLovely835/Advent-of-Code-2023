with open('day6/challenge6.txt', 'r') as file:
    lines = file.readlines()

times = ''.join(str(x) for x in lines[0].split()[1:])
distances = ''.join(str(x) for x in lines[1].split()[1:])

win_count = 0
for j in range(0, int(times)):
    if int(distances) <= j * (int(times) - j):
        win_count += 1

print("Total ways to win multiplied:", win_count)