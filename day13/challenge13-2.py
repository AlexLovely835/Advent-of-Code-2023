with open("day13/challenge13.txt", "r") as file:
    lines = file.readlines()

full = []
hold_group = []
for line in lines:
    if line == '\n':
        full.append(hold_group)
        hold_group = []
    else:
        hold_group.append(line.replace('\n',''))
full.append(hold_group)

def mirror(group):
    for i in range(1, len(group)):
        if sum(sum(1 for u, d in zip(l, r) if u != d) for l, r in zip(reversed(group[:i]), group[i:])) == 1:
            return i*100

    for i in range(1, len(group[0])):
        if sum(sum(1 for l, r in zip(reversed(r[:i]), r[i:]) if l != r) for r in group) == 1:
            return i
        
    group = list(map(''.join, zip(*group)))
    for line in group:
        print(line)
    print("")
    return 0

print("Sum of all results:", sum(mirror(group) for group in full))