N, C = map(int, input().split())
Poses = [int(input()) for _ in range(N)]
Poses.sort()

distLo = 1
distHi = Poses[-1] - Poses[0]
ans = 0

# dist 간격으로 설치했을 때, 공유기 몇 개 설치 가능한지 반환
def solve(dist):
    res = 1
    prevPos = Poses[0]

    for i in range(1, len(Poses)):
        if Poses[i] - prevPos >= dist:
            res += 1
            prevPos = Poses[i]
    
    return res

while distLo <= distHi:
    mid = (distLo + distHi) // 2

    val = solve(mid) # mid 간격으로 공유기 설치했을 때 설치할 수 있는 공유기 개수

    # 간격을 늘려야 하는 경우 = 더 많이 설치되었을 때.
    if val >= C:
        ans = max(ans, mid)
        distLo = mid + 1
    
    # 간격을 줄여야 하는 경우 = 더 조금 설치되었을 때,
    else:
        distHi = mid - 1

print(ans)
