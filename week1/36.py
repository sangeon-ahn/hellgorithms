from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

l = list(permutations(nums, N))

ans = 0
for x in l:
    tempSum = 0
    for i in range(len(list(x)) - 1):
        tempSum += abs(x[i] - x[i + 1])
    
    ans = max(ans, tempSum)

print(ans)
    
    


