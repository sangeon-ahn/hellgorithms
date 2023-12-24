N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = [0, 0]

def check(length, x, y):
    for i in range(length):
        for j in range(length):
            if board[x + i][y + j] != board[x][y]:
                return False
    return True

def recur(length, x, y): # 한 변의 길이, 시작x, 시작y
    if length == 1:
        ans[board[x][y]] += 1
        return
    
    if check(length, x, y):
        ans[board[x][y]] += 1
        return
    
    recur(length // 2, x, y)
    recur(length // 2, x, y + (length // 2))
    recur(length // 2, x + (length // 2), y)
    recur(length // 2, x + (length // 2), y + (length // 2))

recur(N, 0, 0)
print(ans[0])
print(ans[1])