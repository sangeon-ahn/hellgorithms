import sys
from collections import deque
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for i in range(V):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


# 어떻게 풀고 싶나? 1을 넣고 뺀 후, 1과 연결된 노드들 뽑아내서 방문 안햇으면 체크하고 다시 큐에 넣고 그렇게 해서 카운트도 세다가 카운트값 = 노드개수 되면 가중치합 기존 값이랑 비교해서 더 작으면 업데이트. 그렇게 하려면 dfs 해야하는거 아닌가? bfs는 방문체크 초기화가 안되잖아. 그래서 큐에 방문기록도 넣어주면 됨.정점개수 1만개임.
# 그래서 dfs로 풀기? 풀리나? 

vis = [False] * 10001
vis[1] = True
ans = sys.maxsize

def dfs(curPos, weightSum, cnts):
    global ans
    if cnts == V:
        ans = min(ans, weightSum)
        return

    for nxtN, nxtW in graph[curPos]:
        if vis[nxtN]:
            continue

        vis[nxtN] = True
        dfs(nxtN, weightSum + nxtW, cnts + 1)
        vis[nxtN] = False
        
dfs(1, 0, 1) # 현재 위치, 가중치합, 방문카운트

print(ans)




