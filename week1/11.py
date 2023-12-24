import sys
maxNum = -sys.maxsize
maxNumIdx = 0

for i in range(9):
    num = int(input())
    
    if maxNum < num:
        maxNum = num
        maxNumIdx = i + 1

print(maxNum)
print(maxNumIdx)

