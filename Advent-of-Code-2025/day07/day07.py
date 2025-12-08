file = open('input.txt', 'r')

input = []
input2 = []

lines = file.readlines()
for line in lines:
    input.append(list(line.strip('\n')))
    input2.append(list(line.strip('\n')))

def createBeams(x, y, count):
    # return if out of bounds
    if x < 0 or x >= len(input) - 1:
        return count
    if y < 0 or y >= len(input[0]) - 1:
        return count

    if input[x+1][y] == '.':
        input[x][y] = '|'
        count = createBeams(x+1, y, count)
    elif input[x+1][y] == '^':
        input[x][y] = '|'
        count = createBeams(x+1, y-1, count)
        count = createBeams(x+1, y+1, count)
        return count + 1
    else:
        input[x][y] = '|'
    return count

nodeDict = {}
currentNodes = []
def createBeams2(x, y, count):
    # return if out of bounds
    if x < 0:
        return count
    if y < 0 or y >= len(input2[0]) - 1:
        return count

    currentNodes.append((x, y))

    if x >= len(input2) - 1:
        for node in currentNodes:
            if node in nodeDict:
                nodeDict[node] += 1
            else:
                nodeDict[node] = 1
        currentNodes.remove((x, y))
        return count + 1
    
    if (x, y) in nodeDict:
        for node in currentNodes:
            if node != (x, y):
                nodeDict[node] += nodeDict[(x, y)]
        currentNodes.remove((x, y))
        return count + nodeDict[(x, y)]
    else:
        nodeDict[(x, y)] = 0
        if input2[x+1][y] == '.':
            count = createBeams2(x+1, y, count) 
        elif input2[x+1][y] == '^':
            count = createBeams2(x+1, y-1, count) 
            count = createBeams2(x+1, y+1, count) 

    currentNodes.remove((x, y))
    return count

part1Total = createBeams(0, input[0].index('S'), 0)
print('part 1:', part1Total)

part2Total = createBeams2(0, input2[0].index('S'), 0) + 1
print('part 2:', part2Total)
