import sys
N = int(input())
vals = list(map(int, input().split()))
vals.sort()

ans = [0, 0]
res = sys.maxsize
l = 0
r = len(vals) - 1

while l < r:
    candi = vals[l] + vals[r]

    if res > abs(candi):
        ans[0] = vals[l]
        ans[1] = vals[r]
        res = abs(candi)
        
    if candi > 0:
        r -= 1
    elif candi < 0:
        l += 1
    else:
        break
    


print(f"{ans[0]} {ans[1]}")
    

