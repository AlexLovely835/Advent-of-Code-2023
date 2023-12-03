sum = 0

min = {}

with open('day2/challenge2.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace(":", " :").replace(",", " ,").replace(";", "").split()
        line.append(";")
        i = 0
        min["blue"] = 0
        min["green"] = 0
        min["red"] = 0
        while i < len(line):
            if line[i] == "Game":
                i += 1
            elif line[i].isnumeric():
                if int(line[i]) > min[line[i+1]]:
                    min[line[i+1]] = int(line[i])
                i += 1
            elif line[i] == ";":
                sum += (min["green"] * min["blue"] * min["red"])
            i += 1

print("Sum of the powers of all games: ", sum)