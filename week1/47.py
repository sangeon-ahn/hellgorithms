N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]
X.sort()

teamLo = X[0]
teamHi = X[-1]
mid = 0
ans = 0

def solve(teamLevel):
    need = 0

    for level in X:
        if teamLevel > level:
            need += (teamLevel - level)
    
    return need
    


while teamLo <= teamHi:
    mid = (teamLo + teamHi) // 2

    val = solve(mid) # 팀 레벨을 mid로 하기 위해 필요한 레벨양

    # if val <= K:
    #     ans = max(ans, mid)
    #     teamLo = mid + 1
    # else:
    #     teamHi = mid - 1

    # 더 크면 줄어야 함.
    if val > K:
        teamHi = mid - 1
    # 더 작으면 키워야 함, 그리고 일단 갱신
    elif val < K:
        teamLo = mid + 1
        ans = max(ans, mid)
    # 같으면 끝
    else:
        ans = max(ans, mid)
        break

print(ans)
        
