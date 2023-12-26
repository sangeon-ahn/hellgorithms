from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vis = [False] * (N + 1)
ans = 0
q = deque()
q.append(1)
vis[1] = True

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        if not vis[nxt]:
            ans += 1
            vis[nxt] = True
            q.append(nxt)

print(ans)
