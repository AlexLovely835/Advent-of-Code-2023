sum = 0


with open('day4/challenge4.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace('\n', '').split()
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
                        if score == 0:
                            score = 1
                        else:
                            score *= 2
                else:
                    winning.add(line[i])
        sum += score

print("Total score of all cards:", sum)