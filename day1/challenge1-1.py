sum = 0

with open('challenge1.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        for i in range(0, len(line)):
            if line[i].isdigit():
                right = line[i]
        for j in range(len(line)-1, -1, -1):
            if line[j].isdigit():
                left = line[j]
        sum += int(left + right)
    
print('total of all calibration number is: ', sum)