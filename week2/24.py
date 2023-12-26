import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vis = [False] * (N + 1)
parents = [0] * (N + 1)
q = deque()

q.append(1)
vis[1] = True

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        if not vis[nxt]:
            parents[nxt] = cur
            vis[nxt] = True
            q.append(nxt)

for n in parents[2:]:
    print(n)


