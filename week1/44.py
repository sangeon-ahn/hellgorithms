N, M = map(int, input().split())
heights = list(map(int, input().split()))

heightLo = 0
heightHi = 1000000000

ans = 0

def solve(cut):
    res = 0

    for h in heights:
        if cut < h:
            res += h - cut
    
    return res

while heightLo <= heightHi:
    mid = (heightLo + heightHi) // 2

    val = solve(mid)

    if val >= M:
        ans = max(ans, mid)
        heightLo = mid + 1
    else:
        heightHi = mid - 1

print(ans)