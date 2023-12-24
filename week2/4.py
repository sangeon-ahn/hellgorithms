import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]

ans = 1
cur = heights[-1]
heights.pop()

while heights:
    if heights[-1] > cur:
        ans += 1
        cur = heights.pop()
    else:
        heights.pop()

print(ans)



