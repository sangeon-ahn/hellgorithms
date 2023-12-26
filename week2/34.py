from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split())
tomatos = [list(list(map(int, input().rstrip().split())) for _ in range(N)) for _ in range(H)]
q = deque()

unripped = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 0:
                unripped += 1
            elif tomatos[i][j][k] == 1:
                q.append((j, k, i, 0)) # x, y, z

if unripped == 0:
    print(0)
    sys.exit()

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while q:
    curX, curY, curZ, days = q.popleft()

    for i in range(6):
        nx = curX + dx[i]
        ny = curY + dy[i]
        nz = curZ + dz[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
            continue

        if tomatos[nz][nx][ny] == -1 or tomatos[nz][nx][ny] == 1:
            continue

        tomatos[nz][nx][ny] = 1
        unripped -= 1

        if unripped == 0:
            print(days + 1)
            sys.exit()

        q.append((nx, ny, nz, days + 1))

if unripped > 0:
    print(-1)
# 1. 익은 토마토들을 큐에 넣고 뺄 때마다 주변 안익은 토마토 익히고 unripped 제거
# 2. 제거했는데 unripped 0개면 끝
# 3. while 나왔는데 unripped 0개 아니면 -1
