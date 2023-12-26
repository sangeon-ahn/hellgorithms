import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
year = 0

# 빙하 두 영역 체크
    # 영역 개수 확인해서 0개면 0 출력. 2개 이상이면 year 출력. break
# 빙하 녹이고 적용
# 1년 증가

def calContinent():
    q = deque()
    vis = [[False] * M for _ in range(N)]
    areas = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not vis[i][j]:
                areas += 1
                q.append((i, j))

                while q:
                    curX, curY = q.popleft()

                    for k in range(4):
                        nx = curX + dx[k]
                        ny = curY + dy[k]

                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue

                        if board[nx][ny] == 0:
                            continue

                        if vis[nx][ny]:
                            continue

                        vis[nx][ny] = True
                        q.append((nx, ny))
    
    return areas

def getZeros(x, y):
    res = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if board[nx][ny] == 0:
            res += 1

    return res
        

subPendings = [[0] * M for _ in range(N)]
while True:
    # for l in board:
    #     print(l)
    # print()
    cnts = calContinent()
    if cnts > 1:
        print(year)
        break
    elif cnts == 0:
        print(0)
        break

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                zeros = getZeros(i, j)
                subPendings[i][j] = zeros
    
    # for l in subPendings:
    #     print(l)
    # print()
    for i in range(N):
        for j in range(M):
            board[i][j] -= subPendings[i][j]

            if board[i][j] < 0:
                board[i][j] = 0
    
    year += 1
            