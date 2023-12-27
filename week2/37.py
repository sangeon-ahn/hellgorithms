from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegrees = [0] * (N + 1)
q = deque()

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegrees[v] += 1

for i in range(1, N + 1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end = ' ')

    for nxt in graph[cur]:
        indegrees[nxt] -= 1

        if indegrees[nxt] == 0:
            q.append(nxt)

