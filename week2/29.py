from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]
ans = 0
for _ in range(M):
    u, v = map(int, input().split()) # u가 v보다 무겁다.
    graph1[u].append(v)
    graph2[v].append(u)

for i in range(1, N + 1):
    vis = [False] * (N + 1)
    vis[i] = True

    q = deque()
    q.append(i)
    cnts = 0

    while q:
        cur = q.popleft()

        for nxt in graph1[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                cnts += 1
                q.append(nxt)
    
    if cnts > N // 2:
        ans += 1

for i in range(1, N + 1):
    vis = [False] * (N + 1)
    vis[i] = True

    q = deque()
    q.append(i)
    cnts = 0

    while q:
        cur = q.popleft()

        for nxt in graph2[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                cnts += 1
                q.append(nxt)
    
    if cnts > N // 2:
        ans += 1

print(ans)


    


