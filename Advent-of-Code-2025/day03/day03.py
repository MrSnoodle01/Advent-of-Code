file = open('input.txt', 'r')

input = []

lines = file.readlines()
for line in lines:
    input.append(line.strip('\n'))

# part 1
total = 0
for line in input:
    maxNum1 = 0
    maxNum2 = 0
    maxIndex = 0
    for i in range(len(line)-1):
        if int(line[i]) > maxNum1:
            maxNum1 = int(line[i])
            maxIndex = i
    for i in range(maxIndex+1, len(line)):
        if int(line[i]) > maxNum2:
            maxNum2 = int(line[i])
    joltage = str(maxNum1) + str(maxNum2)
    total += int(joltage)
print('part 1:', total)

# part 2
total = 0
index = 0
for line in input:
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    for i in range(12):
        for j in range(index, len(line) - 11 + i):
            if int(line[j]) > digits[i]:
                digits[i] = int(line[j])
                index = j + 1
    stringList = [str(num) for num in digits]
    total += int(''.join(stringList))
print('part 2:', total)