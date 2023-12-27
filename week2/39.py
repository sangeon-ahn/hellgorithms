from collections import deque
import sys, heapq

input = sys.stdin.readline
"""
outdegree 기준, 번호 거꾸로 매기기
deque 말고 최대힙 사용(큰 정점부터 나오도록)

"""
N = int(input().rstrip())
board = [input().rstrip() for _ in range(N)]
graph = [[] for _ in range(N + 1)]

outdegrees = [0] * (N + 1)
indegrees = [0] * (N + 1)

hq = []

for i in range(N):
    for j in range(N):
        if board[i][j] == '1': # i->j 간선 존재
            graph[j + 1].append(i + 1)
            outdegrees[j + 1] += 1
            indegrees[i + 1] += 1

for i in range(1, N + 1):
    if indegrees[i] == 0:
        heapq.heappush(hq, -i) # 최대힙

order = N
numbers = [0] * (N + 1)

while hq:
    cur = -heapq.heappop(hq)
    
    numbers[cur] = order
    order -= 1

    for nxt in graph[cur]:
        indegrees[nxt] -= 1

        if indegrees[nxt] == 0:
            heapq.heappush(hq, -nxt)

if sum(indegrees) != 0:
    print(-1)
else:
    for n in numbers[1:]:
        print(n, end= ' ')

