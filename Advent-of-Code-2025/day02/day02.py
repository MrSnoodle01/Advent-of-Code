values = ''

with open('input.txt', 'r') as file:
    file_content = file.read()

    values = file_content.split(',')

# part 1
invalidIDs = 0
for numRange in values:
    nums = numRange.split('-')
    for i in range(int(nums[0]), int(nums[1]) + 1):
        myStr = str(i)
        if len(myStr) % 2 == 0:
            if myStr[:len(myStr)//2] == myStr[len(myStr)//2:]:
                invalidIDs += i
print("Part 1:", invalidIDs)

# part 2
invalidIDs = 0
for numRange in values:
    nums = numRange.split('-')
    for i in range(int(nums[0]), int(nums[1]) + 1):
        myStr = str(i)
        strLength = len(myStr)
        for length in range(1, strLength // 2 + 1):
            if strLength % length == 0: # length is multiple of strLength
                substring = myStr[:length]
                if substring * (strLength // length) == myStr:
                    invalidIDs += i
                    break
print("Part 2:", invalidIDs)