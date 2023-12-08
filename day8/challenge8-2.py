import math

with open('day8/challenge8.txt', 'r') as file:
    lines = file.readlines()

instructions = lines[0].replace('\n', '')
network = {}

for i in range(2, len(lines)):
    temp = ''.join([char for char in lines[i] if char.isalnum() or char.isspace()]).split()
    network[temp[0]] = {
        'L': temp[1],
        'R': temp[2]
    }

current_nodes = []
for node in network.keys():
    if node[2] == 'A':
        current_nodes.append(node)

steps = []

for i in range(len(current_nodes)):
    steps.append(0)
    while True:
        for inst in instructions:
            current_nodes[i] = network[current_nodes[i]][inst]
            steps[i] += 1
            if current_nodes[i][2] == 'Z':
                break
        if current_nodes[i][2] == 'Z':
            break

answer = math.lcm(*steps)

print('Steps required:', answer)   