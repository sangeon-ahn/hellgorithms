"""
    (charX, charY) -> (itemX, itemY) 가장 짧은 경로
    일단 한바퀴를 돌아야 한다.
    돌려면 겹쳐진 네모 구분가능해야함.

    1. 빨간색은 자신이 어떤 네모칸에 올라가 있는지 확인
    2. 시계방향으로 돌면서 기존 네모칸 외에 다른 네모 만나는지 파악
    3. 다른 네모 만났다면, 현재 네모를 다른 네모와 교체하고 다시 시계방향으로 돌기
    4. 파란색을 만날때까지 반복

    겹친다는 것은 동서남북이 모두 True인 경우.
    1. 50*50 boards를 만듬
    2. 선이 그려지는 곳에 True
    3. 빨간색은 해당 위치에서 시계방향 이동
        - True인 쪽으로 이동
        - 여러군대가 True면 겹치는 곳임. 시계방향이 쪽으로 이동
""" 


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[False] * 51 for _ in range(51)]
    
    dic = {}
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for idx, rec in enumerate(rectangle):
        [leftX, leftY, rightX, rightY] = rec
        dic[(leftX, leftY)] = idx
        dic[(rightX, rightY)] = idx

        for i in range(leftY, rightY + 1):
            board[leftX][i] = (True, idx)
            board[rightX][i] = (True, idx)
        
        for i in range(leftX, rightX + 1):
            board[i][leftY] = (True, idx)
            board[i][rightY] = (True, idx)
        
    board[characterX][characterY] = (False)

    curX, curY = characterX, characterY
    steps = 0
    curDir = 0
    saved = 0

    while True:
        print(curX, curY)
        cnts = 0
        points = []
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if nx <= 0 or nx >= 51 or ny <= 0 or ny >= 51:
                continue

            if board[nx][ny][0] and board[curX][cu]:
                cnts += 1
                points.append(i)
        
        if cnts == 1:
            curX += dx[points[0]]
            curY += dy[points[0]]
            
            curDir = points[0]
        
        elif cnts == 2:
            curX += dx[points[0]]
            curY += dy[points[0]]
            curDir = points[0]
            
        elif cnts > 2: # 경우의 수 2개 이상. -> 시계 반대방향
            curDir = (curDir + 1) % 4
            curX += dx[curDir]
            curY += dy[curDir]

        board[curX][curY] = False
        steps += 1

        if curX == itemX and curY == itemY:
            saved = steps

        if curX == characterX and curY == characterY:
            break
    
    return min(saved, steps - saved)

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
sol = solution(rectangle, characterX, characterY, itemX, itemY)
print(sol)
