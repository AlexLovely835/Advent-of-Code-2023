import functools

rows = []

with open("day12/challenge12.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    temp = line.split()
    rows.append((temp[0], tuple(int(x) for x in temp[1].replace('\n', '').split(','))))

@functools.cache
def countSolutions(problem, lengths, current=0):
    if problem == '':
        if not lengths and current == 0:
            return 1
        else:
            return 0
        
    count = 0

    if problem[0] == '?':
        chars = ['.', '#']
    else:
        chars = problem[0]

    for char in chars:
        if char == '#':
            count += countSolutions(problem[1:], lengths, current + 1)
        else:
            if current > 0:
                if lengths and lengths[0] == current:
                    count += countSolutions(problem[1:], lengths[1:])
            else:
                count += countSolutions(problem[1:], lengths)
    return count

sum = 0
for problem, lengths in rows:
    sum += countSolutions("?".join([problem] * 5) + '.', lengths * 5)

print("The total number of solutions is:", sum)