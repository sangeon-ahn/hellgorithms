from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

vis = [False] * (N + 1)
q = deque()
ans = []

vis[X] = True
q.append((X, 0))

while q:
    curPos, curDist = q.popleft()

    for nxt in graph[curPos]:
        if not vis[nxt]:
            vis[nxt] = True
            if curDist + 1 < K:
                q.append((nxt, curDist + 1))
            elif curDist + 1 == K:
                ans.append(nxt)
            else:
                break

if not ans:
    print(-1)
else:
    ans.sort()
    for n in ans:
        print(n)
