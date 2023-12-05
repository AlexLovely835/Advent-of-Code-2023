sum = 0
card_counts = {}

with open('day4/challenge4.txt', 'r') as file:
    lines = file.readlines()

for i in range(0, len(lines)):
    card_counts[i] = 1

for j in range(0, len(lines)):
    line = lines[j].replace('\n', '').split()
    have = False
    winning = set()
    score = 0
    for i in range(2, len(line)):
        if line[i] == "|":
            have = True
        else:
            # I feel very sick today and my head is cloudy so
            # that's my excuse for this heavily nested garbage
            if have:
                if line[i] in winning:
                    score += 1
            else:
                winning.add(line[i])
    for k in range(j, j + score):
        try:
            card_counts[k+1] += card_counts[j]
        except:
            break
    
for i in range(0, len(lines)):
    sum += card_counts[i]

print("Total number of cards:", sum)