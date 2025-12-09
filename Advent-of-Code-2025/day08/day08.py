import math
import sys

file = open('input.txt', 'r')

input = []

lines = file.readlines()
for line in lines:
    input.append(list(line.strip('\n').split(',')))

for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])

# part 1
circuits = []
usedBoxes = []
oldLength = 0
for i in range(10):
    shortestLength = sys.maxsize
    box1 = ''
    box2 = ''
    for j in range(len(input)):
        for k in range(j, len(input)):
            first = input[j]
            second = input[k]
            newLength = math.sqrt((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2 + (first[2] - second[2]) ** 2)
            if newLength < shortestLength and newLength > oldLength:
                shortestLength = newLength
                box1 = first
                box2 = second

    oldLength = shortestLength

    # print('boxes', [box1, box2], shortestLength)

    newCircuit = True
    # if both boxes have been used before then combine their circuits
    # or do nothing if they are already in the same circuit
    if box1 in usedBoxes and box2 in usedBoxes:
        box1Circuit = -1
        box2Circuit = -1
        for i in range(len(circuits)):
            if box1 in circuits[i] and box2 not in circuits[i]:
                box1Circuit = i
            if box2 in circuits[i] and box1 not in circuits[i]:
                box2Circuit = i
        if box1Circuit != -1 and box2Circuit != -1:
            circuits[box1Circuit].extend(circuits[box2Circuit])
            circuits.remove(circuits[box2Circuit])
        newCircuit = False
    else: # if one is a new box then check to see if the connecting box is already in a circuit, otherwise make a new one
        for i in range(len(circuits)):
            if box1 in circuits[i] and box2 not in circuits[i]:
                circuits[i].append(box2)
                newCircuit = False
            elif box2 in circuits[i] and box1 not in circuits[i]:
                circuits[i].append(box1)
                newCircuit = False  
            elif box1 in circuits[i] and box2 in circuits[i]:
                newCircuit = False

        # make a new circuit
        if newCircuit:
            circuits.append([box1, box2])

    usedBoxes.append(box1)
    usedBoxes.append(box2)

circuits = sorted(circuits, key=len, reverse=True)

total = 1
for i in range(3):
    total *= len(circuits[i])

print("part 1:", total)


# part 2
circuits = [[0]]
usedBoxes = []
oldLength = 0
b = 0
final = (0, 0)
while len(circuits) > 1 or len(circuits[0]) < 20 or b < 5:
    if b == 0:
        circuits.remove([0])
    b += 1
    shortestLength = sys.maxsize
    box1 = ''
    box2 = ''
    for j in range(len(input)):
        for k in range(j, len(input)):
            first = input[j]
            second = input[k]
            newLength = math.sqrt((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2 + (first[2] - second[2]) ** 2)
            if newLength < shortestLength and newLength > oldLength:
                shortestLength = newLength
                box1 = first
                box2 = second

    oldLength = shortestLength

    newCircuit = True
    # if both boxes have been used before then combine their circuits
    # or do nothing if they are already in the same circuit
    if box1 in usedBoxes and box2 in usedBoxes:
        box1Circuit = -1
        box2Circuit = -1
        for i in range(len(circuits)):
            if box1 in circuits[i] and box2 not in circuits[i]:
                box1Circuit = i
            if box2 in circuits[i] and box1 not in circuits[i]:
                box2Circuit = i
        if box1Circuit != -1 and box2Circuit != -1:
            circuits[box1Circuit].extend(circuits[box2Circuit])
            circuits.remove(circuits[box2Circuit])
        newCircuit = False
    else: # if one is a new box then check to see if the connecting box is already in a circuit, otherwise make a new one
        for i in range(len(circuits)):
            if box1 in circuits[i] and box2 not in circuits[i]:
                circuits[i].append(box2)
                newCircuit = False
            elif box2 in circuits[i] and box1 not in circuits[i]:
                circuits[i].append(box1)
                newCircuit = False  
            elif box1 in circuits[i] and box2 in circuits[i]:
                newCircuit = False

        # make a new circuit
        if newCircuit:
            circuits.append([box1, box2])

    usedBoxes.append(box1)
    usedBoxes.append(box2)
    final = (box1, box2)

circuits = sorted(circuits, key=len, reverse=True)

total = 1
total = final[0][0] * final[1][0]
print("part 2:", total)
