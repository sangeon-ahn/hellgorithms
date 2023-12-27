from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
outdegrees = [0] * (N + 1)
indegrees = [0] * (N + 1)
pieces = [0] * (N + 1)
pieces[N] = 1
basics = []
for _ in range(M):
    u, v, w = map(int, input().split()) # u를 만드는데 v w개 필요
    outdegrees[u] += 1 # 상위 부품들은 outdegree ++
    indegrees[v] += 1
    graph[u].append((v, w))

for i in range(1, N + 1):
    if outdegrees[i] == 0:
        basics.append(i)

q = deque()
q.append(N)

while q:
    cur = q.popleft()
    for nxt, w in graph[cur]:
        indegrees[nxt] -= 1
        
        pieces[nxt] += pieces[cur] * w
        
        if indegrees[nxt] == 0:
            q.append(nxt)

for i in range(len(basics)):
    print(f"{basics[i]} {pieces[basics[i]]}")
