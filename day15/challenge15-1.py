with open("day15/challenge15.txt", "r") as file:
    sequences = [seq.replace('\n', '') for seq in file.read().split(',')]

for seq in sequences:
    current = 0
    for char in seq:
        current += ord(char)
        current *= 17
        current %= 256
    sum += current

print("Sum of all hash values:", sum)
