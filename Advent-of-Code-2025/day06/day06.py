file = open('input.txt', 'r')

input = []
input1 = []

lines = file.readlines()
for line in lines:
    input1.append(list(line.strip('\n').split(' ')))
    input.append(line)

newInput = []
for i in range(len(input1)):
    tempList = [item for item in input1[i] if item != '']
    newInput.append(tempList)

total = 0
for i in range(len(newInput[0])):
    if newInput[len(newInput)-1][i] == '*':
        tempTotal = 1
    else:
        tempTotal = 0

    for j in range(len(newInput)-1):  
        if newInput[len(newInput)-1][i] == '*':
            tempTotal *= int(newInput[j][i])
        else:
            tempTotal += int(newInput[j][i])

    total += tempTotal
print('part 1:', total)

newInput = []
for i in range(len(input)):
    tempList = []
    numSpaces = 0
    for j in range(len(input[len(input)-1])):
        if input[len(input)-1][j] != ' ':
            tempList.append(input[i][j-numSpaces-1:j-1])
            numSpaces = 0
        else:
            numSpaces += 1
    newInput.append(tempList)

for i in newInput:
    i.pop(0)

total = 0
for i in range(len(newInput[0])):
    if '*' in newInput[len(newInput)-1][i]:
        tempTotal = 1
    else:
        tempTotal = 0

    longest = 0
    for j in range(len(newInput)-1):  
        if len(newInput[j][i]) > longest:
            longest = len(newInput[j][i])

    nums = [''] * longest
    for j in range(len(newInput)-1):  
        newNum = ''
        for k in range(longest):
            if len(newInput[j][i]) > k:
                nums[k] += newInput[j][i][k]

    for j in nums:
        if '*' in newInput[len(newInput)-1][i]:
            tempTotal *= int(j.replace(" ", ""))
        else:
            tempTotal += int(j.replace(" ", ""))

    total += tempTotal
print('part 2:', total)