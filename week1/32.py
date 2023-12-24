import sys
input = sys.stdin.readline

N = int(input())
cnts = [0 for _ in range(10001)]
maxNum = 0

for _ in range(N):
    num = int(input())

    if maxNum < num:
        maxNum = num
    cnts[num] += 1

for i in range(1, maxNum + 1):
    if cnts[i] != 0:
        for _ in range(cnts[i]):
            print(i)

    
