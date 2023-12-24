from itertools import permutations

N = int(input())
K = int(input())
nums = [input() for _ in range(N)]

ans = set()

permus = list(permutations(nums, K))

for i in range(len(permus)):
    num = ""
    
    for j in range(K):
        num += permus[i][j]
    
    ans.add(num)

print(len(ans))

