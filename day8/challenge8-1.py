with open('day8/challenge8.txt', 'r') as file:
    lines = file.readlines()

instructions = lines[0].replace('\n', '')
network = {}

for i in range(2, len(lines)):
    temp = ''.join([char for char in lines[i] if char.isalpha() or char.isspace()]).split()
    network[temp[0]] = {
        'L': temp[1],
        'R': temp[2]
    }

current_node = 'AAA'
steps = 0

while True:
    for inst in instructions:
        current_node = network[current_node][inst]
        steps += 1
        if current_node == 'ZZZ':
            break
    if current_node == 'ZZZ':
        break

print('Steps required:', steps)       