sum = 0
num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open('challenge1.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        for key, value in num_dict.items():
            line = line.replace(key, key[0] + value + key[-1])
        for i in range(0, len(line)):
            if line[i].isdigit():
                right = line[i]
        for j in range(len(line)-1, -1, -1):
            if line[j].isdigit():
                left = line[j]
        print(line, ":", left + right)
        sum += int(left + right)
    
print('total of all calibration number is: ', sum)