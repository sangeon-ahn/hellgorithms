from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
board = [[] for _ in range(R)]

for i in range(R):
    s = input()
    for ch in s:
        board[i].append(ch)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
src = (0, 0)
dst = (0, 0)

waters = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            src = (i, j)
        elif board[i][j] == 'D':
            dst = (i, j)
        elif board[i][j] == '*':
            waters.append((i, j))

q = deque() # (x, y, 시간, 타입 - 고슴도치, 물)
q.append((src[0], src[1], 0, 1)) 
for water in waters:
    q.append((water[0], water[1], 0, -1))

while q:
    curX, curY, time, tp = q.popleft()
    
    # 고슴도친데 이미 죽었으면 패스
    if tp == 1 and board[curX][curY] != 'S':
        continue

    for i in range(4):
        nx = curX + dx[i]
        ny = curY + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if board[nx][ny] == 'X' or board[nx][ny] == '*':
            continue
        
        # 빈공간이면,
        if board[nx][ny] == '.':
            # 고슴도치면,
            if tp == 1:
                board[nx][ny] = 'S'
                board[curX][curY] = '.'

                q.append((nx, ny, time + 1, tp))
            
            # 물이면,
            else:
                board[nx][ny] = '*'
                q.append((nx, ny, time + 1, tp))
        
        # 고슴도치면,
        elif board[nx][ny] == 'S':
            # 내가 물이면,
            if tp == -1:
                board[nx][ny] = '*'
                q.append((nx, ny, time + 1, tp))
        
        # 목적지면,
        elif board[nx][ny] == 'D':
            # 내가 고슴도치면,
            if tp == 1:
                print(time + 1)
                sys.exit()

print("KAKTUS")


    


