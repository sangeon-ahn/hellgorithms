from collections import deque
import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))

for l in graph:
    l.sort(key = lambda x : x[1])

src, dst = map(int, input().rstrip().split())
ans = 0
vis = [False] * (N + 1)
dist = [sys.maxsize] * (N + 1)

dist[src] = 0
vis[src] = True

q = []
heapq.heappush(q, (dist[src], src))

while q:
    curDist, curPos = heapq.heappop(q)

    if curDist != dist[curPos]:
        continue

    for nxt, w in graph[curPos]:
        if dist[nxt] > curDist + w:
            dist[nxt] = curDist + w
            heapq.heappush(q, (curDist + w, nxt))

print(dist[dst])
        




