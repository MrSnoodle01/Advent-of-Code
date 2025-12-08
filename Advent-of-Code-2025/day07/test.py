import time

file = open('input.txt', 'r')

input = []

lines = file.readlines()
for line in lines:
    # input.append(list(line.strip('\n').split(' ')))
    input.append(list(line.strip('\n')))

def createBeams(x, y, count):
    # return if out of bounds
    if x < 0 or x >= len(input[0]):
        return count
    if y < 0 or y >= len(input):
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

def createBeams2(x, y, count):
    # return if out of bounds
    if x < 0 or x >= len(input[0]):
        return count + 1
    if y < 0 or y >= len(input):
        return count
        
    if input[x+1][y] == '.':
        input[x][y] = '|'
        count = createBeams2(x+1, y, count)
    elif input[x+1][y] == '^':
        input[x][y] = '|'
        count = createBeams2(x+1, y-1, count)
        count = createBeams2(x+1, y+1, count)
    else:
        input[x][y] = '|'
    input[x][y] = '.'
    return count


# part1Total = createBeams(0, input[0].index('S'), 0)
# print(part1Total)

startTime = time.time()
part2Total = createBeams2(0, input[0].index('S'), 0)
print('part 2:', part2Total)
endTime = time.time()
print("Execution time:", endTime-startTime)
for row in input:
    for item in row:
        print(f"{item:0}", end="")  # Adjust '4' for desired column width
    print()  # New line after each row