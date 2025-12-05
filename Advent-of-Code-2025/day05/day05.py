file = open('input.txt', 'r')

idRanges = []
tempRanges = []
items = []
gotAllRanges = False

lines = file.readlines()
for line in lines:
    if line == "\n":
        gotAllRanges = True
    elif gotAllRanges == False:
        idRanges.append(list(line.strip('\n').split('-')))
        tempRanges.append(list(line.strip('\n').split('-')))
    else:
        items.append(int(line.strip('\n')))

# part 1
freshCount = 0
for i in items:
    for j in idRanges:
        if i >= int(j[0]) and i <= int(j[1]):
            freshCount += 1
            break

print('part 1:', freshCount)

# part 2
for i in idRanges:
    i[0] = int(i[0])
    i[1] = int(i[1])

# remove duplicate entries
for i in range(len(idRanges)):
    for j in range(len(idRanges)):
        if i != j:
            if idRanges[i][0] == idRanges[j][0]:
                if idRanges[i][1] < idRanges[j][1]:
                    idRanges[i] = [0,0]
                else:
                    idRanges[j] = [0,0]
            if idRanges[i][1] == idRanges[j][1]:
                if idRanges[i][0] > idRanges[j][0]:
                    idRanges[i] = [0,0]
                else:
                    idRanges[j] = [0,0]

# remove overlapping entries
for i in range(len(idRanges)):
    for j in range(len(idRanges)):
        if j != i:
            if idRanges[j][1] >= idRanges[i][0] and idRanges[j][0] < idRanges[i][0]:
                if idRanges[j][1] + 1 < idRanges[i][1]:
                    idRanges[i][0] = idRanges[j][1] + 1
                else:
                    idRanges[i] = [0,0]

freshCount = 0
for i in idRanges:
    if i[0] != 0 and i[1] != 0:
        freshCount += i[1] - i[0] + 1

print('part 2:', freshCount)
