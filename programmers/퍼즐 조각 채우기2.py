"""
    노멀라이즈 함수
"""
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def normalize_set(before):
    min_x, min_y = min(before)
    after = {(x - min_x, y - min_y) for x, y in before}
    return after

def spin_set(original):
    spin_90 = set()
    spin_180 = set()
    spin_270 = set()
    while original:
        x, y = original.pop()
        spin_90.add((y, -x))
        spin_180.add((-x, -y))
        spin_270.add((-y, x))
    return spin_90, spin_180, spin_270

def dfs(a, b, height, width, board, aim):
    idx_set = {(a, b), } # visited 역할
    
    q = {(a, b), }
    
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and (nx, ny) not in idx_set and board[nx][ny] == aim:
                idx_set.add((nx, ny))
                q.add((nx, ny))

    length = len(idx_set)

    spin_90, spin_180, spin_270 = spin_set(set(idx_set))

    spin_0 = normalize_set(idx_set)
    spin_90 = normalize_set(spin_90)
    spin_180 = normalize_set(spin_180)
    spin_270 = normalize_set(spin_270)

    return length, idx_set, spin_0, spin_90, spin_180, spin_270

def solution(game_board, table):
    width = len(game_board)
    board_visited = set()
    board_dict = dict()
    table_visited = set()
    table_dict = dict()

    for i in range(width):
        for j in range(width):
            # game_board에 해당하는 로직
            if game_board[i][j] == 0 and (i, j) not in board_visited: # 빈 공간 발견시,
                empty_length, empty_visited, empty_0, empty_90, empty_180, empty_270 = dfs(i, j, width, width, game_board, 0)
                board_visited |= empty_visited # set간에 합집합 연산하는 것

                if empty_length not in board_dict.keys():
                    board_dict[empty_length] = [[empty_0, empty_90, empty_180, empty_270], ]
                else:
                    board_dict[empty_length].append([empty_0, empty_90, empty_180, empty_270])
            
            # table에 해당하는 로직. game_board와 독립적으로 작동함.
            if table[i][j] == 1 and (i, j) not in table_visited:
                table_length, block_visited, table_0, table_90, table_180, table_270 = dfs(i, j, width, width, table, 1)
                table_visited |= block_visited
                if table_length not in table_dict.keys():
                    table_dict[table_length] = [[table_0, table_90, table_180, table_270], ]
                else:
                    table_dict[table_length].append([table_0, table_90, table_180, table_270])
    
    answer = 0
    fit_visited = set()

    for block_length in table_dict.keys():
        if block_length in board_dict.keys():
            block_list = table_dict[block_length]
            empty_list = board_dict[block_length]

            for block_idx in range(len(block_list)):
                for empty_idx in range(len(empty_list)):
                    if (block_length, empty_idx) in fit_visited: # empty_idx: empty_list는 2차원 리스트고, empty_idx는 한 공간을 나타냄.따라서 (block_length, empty_idx)가 이미 있다는건, 해당 공간을 이미 채웠다는 뜻.
                        continue
                    
                    else:
                        flag = False

                        for i in range(4): # 0,90,180,270
                            if flag:
                                break

                            for j in range(i, 4):
                                if block_list[block_idx][i] == empty_list[empty_idx][j]:
                                    flag = True
                                    fit_visited.add((block_length, empty_idx))
                                    answer += block_length
                                    break
                        
                        if flag:
                            break
    
    return answer
                            






