sum = 0

with open('day9/challenge9.txt', 'r') as file:
    lines = file.readlines()

seqs = []
for line in lines:
    temp = line.split()
    seqs.append([int(x) for x in temp])

def mapSequence(seq):
    step_changes = [seq]
    current = 0
    while not all (x == 0 for x in step_changes[current]):
        seq = step_changes[current]
        step_changes.append([])
        for i in range(1, len(step_changes[current])):
            step_changes[current+1].append(seq[i] - seq[i-1])
        current += 1
    return step_changes

def findNext(seq):
    seqMap = mapSequence(seq)

    for i in range(len(seqMap)-1, -1, -1):
        try: 
            next_value = seqMap[i][-1] + seqMap[i+1][-1]
        except: 
            next_value = 0
        seqMap[i].append(next_value)
    return seqMap[0][-1]


for seq in seqs:
    sum += findNext(seq)

print("Sum of extrapolated values:", sum)