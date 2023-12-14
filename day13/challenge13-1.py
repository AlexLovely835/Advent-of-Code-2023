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
        if all(l == r for l, r in zip(reversed(group[:i]), group[i:])):
            return i*100

    for i in range(1, len(group[0])):
        if all(all(l == r for l, r in zip(reversed(r[:i]), r[i:])) for r in group):
            return i
        
    group = list(map(''.join, zip(*group)))
    for line in group:
        print(line)
    print("")
    return 0

print("Sum of all results:", sum(mirror(group) for group in full))