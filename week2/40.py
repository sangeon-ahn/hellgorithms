from collections import deque
import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
indegrees = [0] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    indegrees[v] += 1

src, dst = map(int, input().split())
dist = [0] * (N + 1)
pq = []
paths = [[] for _ in range(N + 1)]

heapq.heappush(pq, (0, src))

while pq:
    curDist, curPos = heapq.heappop(pq)
    curDist *= -1

    for nxt, w in graph[curPos]:
        indegrees[nxt] -= 1

        if dist[nxt] < curDist + w: # 새 경로로 갱신
            dist[nxt] = curDist + w
            paths[nxt] = [curPos]

        elif dist[nxt] == curDist + w: # 기존 경로에 추가
            paths[nxt].append(curPos)
            
        if indegrees[nxt] == 0:
            heapq.heappush(pq, (-dist[nxt], nxt))


routes = set()
q = deque()
q.append(dst)

while q:
    nextCity = q.popleft()

    for curCity in paths[nextCity]:
        if (curCity, nextCity) not in routes:
            routes.add((curCity, nextCity)) 
            q.append(curCity)

print(dist[dst])
print(len(routes))



