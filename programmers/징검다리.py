import time
def solve(dist, rocks):
    res = 0

    curPos = 0
    for i in range(1, len(rocks)):
        if rocks[i] - curPos >= dist:
            curPos = rocks[i]
        else: # i번재 돌 부숨
            res += 1
    
    return res
        

def solution(distance, rocks, n):
    answer = 0

    st = 1
    en = distance

    rocks.append(distance)
    rocks.sort()

    while st <= en:
        mid = (st + en) // 2
        val = solve(mid, rocks) # 최소 거리가 mid일 때, 몇개 부숴야 하는지,
        if val < n:
            answer = mid
            st = mid + 1
        elif val > n:
            en = mid - 1
        else:
            answer = mid
            st = mid + 1

    return int(answer)

sol = solution(25, [2, 14, 11, 21, 17], 2)
print(sol)