with open("day15/challenge15.txt", "r") as file:
    sequences = [seq.replace('\n', '') for seq in file.read().split(',')]

boxes =  [ [] for _ in range(256) ] 

def hash(seq):
    current = 0 
    for char in seq:
        current += ord(char)
        current *= 17
        current %= 256
    return current

def find_index(box, label):
    for i in range(len(boxes[box])):
        if label == boxes[box][i][0]:
            print("return")
            return i
            

for seq in sequences:
    label_length = 0
    for i in range(len(seq)):
        if not seq[i].isalpha():
            label_length = i
            break
    label = seq[0:i]
    if seq[i] == "=":
        value = int(seq[i+1])
    else:
        value = None
    box = hash(label)
    index = find_index(box, label)
    if value != None:
        if index == None:
            boxes[box].append([label, value])
        else:
            boxes[box][index][1] = value
    else:
        if index != None:
            boxes[box].pop(index)

for box in boxes:
    if box != []:
        print(box)


sum = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        sum += ((i+1) * (j+1) * boxes[i][j][1])

print("Focusing power of entire lens configuration:", sum)