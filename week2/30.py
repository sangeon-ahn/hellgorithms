from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

for i in range(N):
    line = input().rstrip()
    
    for j in range(len(line)):
        board[i][j] = line[j]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
ans = sys.maxsize
vis = [[False] * M for _ in range(N)]
vis[0][0] = True

q.append((0, 0, 1))

while q:
    curX, curY, cnts = q.popleft()

    if curX == N - 1 and curY == M - 1:
        ans = min(ans, cnts)
        continue

    for i in range(4):
        nx = curX + dx[i]
        ny = curY + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if board[nx][ny] == '0':
            continue

        if vis[nx][ny]:
            continue

        vis[nx][ny] = True
        q.append((nx, ny, cnts + 1))

print(ans)

        