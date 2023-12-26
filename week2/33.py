from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
board = [input().rstrip() for _ in range(N)]

q = deque()
vis = [[False] * (N + 1) for _ in range(N + 1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q.append((0, 0, 0)) # (x, y, 검은방 들어간 횟수)

blackCnts = [[sys.maxsize] * N for _ in range(N)]
blackCnts[0][0] = 0
ans = sys.maxsize

while q:
    curX, curY, bcnts = q.popleft()

    if curX == N - 1 and curY == N - 1:
        ans = min(ans, bcnts)
        continue

    for i in range(4):
        nx = curX + dx[i]
        ny = curY + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if board[nx][ny] == '1':
            if blackCnts[nx][ny] > bcnts:
                blackCnts[nx][ny] = bcnts
                q.append((nx, ny, bcnts)) 

        elif board[nx][ny] == '0':
            if blackCnts[nx][ny] > bcnts + 1:
                blackCnts[nx][ny] = bcnts + 1
                q.append((nx, ny, bcnts + 1))

print(ans)