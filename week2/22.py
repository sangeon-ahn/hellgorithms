from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vis = [False] * (N + 1)
ans = 0

def bfs(node):
    vis[node] = True
    q = deque()

    q.append(node)

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                q.append(nxt)




for i in range(1, N + 1):
    if vis[i]:
        continue

    ans += 1
    bfs(i)

print(ans)
