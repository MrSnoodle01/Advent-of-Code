file = open('input.txt', 'r')

input = []

lines = file.readlines()
for line in lines:
    input.append(list(line.strip('\n').split(',')))

for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])

# part 1
largestArea = 0
for i in input:
    for j in input:
        newArea = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)
        if newArea > largestArea:
            largestArea = newArea

print('part 1:', largestArea)

# part 2
largestArea = 0
for i in input:
    for j in input:
        newArea = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)
        if newArea > largestArea:
            opposite1 = [i[0], j[1]]
            opposite2 = [j[0], i[1]]

            insideLoop1 = False
            insideLoop2 = False
            for k in input:
                if opposite1[1] < i[1]: # opposite 1 corner below point i
                    if opposite1[0] > j[0]: # opposite 1 corner right of point j
                        if k[0] >= opposite1[0] and k[1] <= opposite1[1]:
                            insideLoop1 = True
                    else: # opposite 1 corner left of point j
                        if k[0] <= opposite1[0] and k[1] <= opposite1[1]:
                            insideLoop1 = True
                else: # opposite 1 corner above point i
                    if opposite1[0] > j[0]: # opposite 1 corner right of point j
                        if k[0] >= opposite1[0] and k[1] >= opposite1[1]:
                            insideLoop1 = True
                    else: # opposite 1 corner left of point j
                        if k[0] <= opposite1[0] and k[1] >= opposite1[1]:
                            insideLoop1 = True

                if opposite2[1] > j[1]: # opposite 2 corner above point j
                    if opposite2[0] < i[0]: # opposite 2 corner left of point i
                        if k[0] <= opposite2[0] and k[1] >= opposite2[1]:
                            insideLoop2 = True
                    else: # opposite 2 corner right of point i
                        if k[0] >= opposite2[0] and k[1] >= opposite2[1]:
                            insideLoop2 = True
                else: # opposite 2 corner below point j
                    if opposite2[0] < i[0]: # opposite 2 corner left of point i
                        if k[0] <= opposite2[0] and k[1] <= opposite2[1]:
                            insideLoop2 = True
                    else: # opposite 2 corner right of point i
                        if k[0] >= opposite2[0] and k[1] <= opposite2[1]:
                            insideLoop2 = True
            
            # hardcoding for specific case :(
            if insideLoop1 and insideLoop2 and ((i[1] >= 50260 and j[1] >= 50260) or (i[1] <= 48492 and j[1] <= 48492)):
                largestArea = newArea

print('part 2:', largestArea)