file = open('testinput.txt', 'r')

input = []

lines = file.readlines()
for line in lines:
    input.append(list(line.strip('\n')))

x = [0, 0, 1, 1, 1, -1, -1, -1]
y = [1, -1, 0, 1, -1, 0, 1, -1]


# part 1
adjacentNum = 0
total = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        adjacentNum = 0
        if input[i][j] == '@':
            for k in range(len(x)):
                if i + x[k] >= 0 and i + x[k] < len(input):
                    if j + y[k] >= 0 and j + y[k] < len(input[i + x[k]]):
                        if input[i + x[k]][j + y[k]] == '@':
                            adjacentNum += 1
            if adjacentNum < 4:
                total += 1

print('part 1:', total)

# part 2
adjacentNum = 0
total = 0
oldTotal = total
removePaper = True

while removePaper:
    for i in range(len(input)):
        for j in range(len(input[i])):
            adjacentNum = 0
            if input[i][j] == '@':
                for k in range(len(x)):
                    if i + x[k] >= 0 and i + x[k] < len(input):
                        if j + y[k] >= 0 and j + y[k] < len(input[i + x[k]]):
                            if input[i + x[k]][j + y[k]] == '@':
                                adjacentNum += 1
                if adjacentNum < 4:
                    total += 1
                    input[i][j] = '.'
    if total == oldTotal: 
        removePaper = False
    else:
        oldTotal = total

print('part 2:', total)
