from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
dirs = deque(list(input().split() for _ in range(L)))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dir = 0

board = [[0] * (N + 1) for _ in range(N + 1)]

for apple in apples:
    board[apple[0]][apple[1]] = 1

headX = 1
headY = 1
board[headX][headY] = -1

tails = deque([(headX, headY)])

gameTime = 1

while True:
    # 뱀 이동.
    newHeadX = headX + dx[dir]
    newHeadY = headY + dy[dir]

    # 칸 밖이면,
    if newHeadX > N or newHeadX < 1 or newHeadY > N or newHeadY < 1:
        print(gameTime)
        break

    # 뱀 있으면,
    if board[newHeadX][newHeadY] == -1:
        print(gameTime)
        break

    # 사과 있으면
    if board[newHeadX][newHeadY] == 1:
        tails.append((newHeadX, newHeadY))
        board[newHeadX][newHeadY] = -1
    
    # 사과 없으면,
    elif board[newHeadX][newHeadY] == 0:
        tails.append((newHeadX, newHeadY))
        board[newHeadX][newHeadY] = -1
        
        # 꼬리 제거
        if tails:
            tail = tails.popleft()
            board[tail[0]][tail[1]] = 0
    
    # 머리 옮기고
    headX = newHeadX
    headY = newHeadY
    board[headX][headY] = -1

    # 방향 바꿔주기
    if dirs and int(dirs[0][0]) == gameTime:
        if dirs[0][1] == 'D':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        dirs.popleft()

    gameTime += 1
    



    

