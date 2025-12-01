file = open('input.txt', 'r')

input = []

lines = file.readlines()
for line in lines:
    temp = []
    temp.append(line[:1])
    temp.append(int(line[1:8].rstrip('\n')))
    input.append(temp)

# part 1
dial = 50
ans = 0

for line in input:
    if line[0] == 'L':
        dial -= line[1]
        if dial < 0:
            dial %= 100
    else:
        dial += line[1]
        if dial > 99:
            dial %= 100
    if dial == 0:
        ans += 1

print('part 1:', ans)

# part 2
dial = 50
ans = 0

for line in input:
    prevDial = dial
    if line[0] == 'L':
        dial -= line[1]
        if dial < 0:
            numZeros = 1
            numZeros += abs(int(dial / 100)) 
            if prevDial == 0:
                numZeros -= 1
            if dial % 100 == 0:
                numZeros -= 1
            ans += numZeros
            
            dial %= 100
    else:
        dial += line[1]
        if dial > 99:
            if dial != 100:
                numZeros = int(dial / 100)
                if dial % 100 == 0:
                    numZeros -= 1
                ans += numZeros
            dial %= 100
    if dial == 0:
        ans += 1

print('part 2:', ans)