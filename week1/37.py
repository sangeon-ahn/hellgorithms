import sys

N = int(input())
weights = [list(map(int, input().split())) for _ in range(N)]

isVisited = [False for _ in range(N + 1)] 
ans = sys.maxsize

def recur(n, cnts, cur, costs):
    global ans
    if n == cnts: # 자기 자신으로 돌아와야 함.
        if weights[cur][0] != 0:
            ans = min(ans, costs + weights[cur][0])
        return
    
    for i in range(n):
        if weights[cur][i] != 0 and not isVisited[i]:
            isVisited[i] = True
            recur(n, cnts + 1, i, costs + weights[cur][i])
            isVisited[i] = False
        
isVisited[0] = True
recur(N, 1, 0, 0) # 도시 개수, 이동한 도시 개수, 현재 도시 위치, 현재 비용 합
print(ans)


