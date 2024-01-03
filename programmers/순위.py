"""
플루이드 와샬 기법 써서 풀기
- n*n 배열 필요, 초기값 0
- 이후, 지면 -1, 이기면 1 채워넣기
- 3중 for문 끝난 후, 한명에 대해 모든 셀이 -1 아니면 1이면 순위 매기기 가능 -> 답에 추가
- 0이 하나라도 있으면 순위 결정 불가
- 
"""

def solution(n, results):
    answer = 0
    
    fluids = [[0] * n for _ in range(n)]
    
    for res in results:
        u, v = res
        fluids[u-1][v-1] = 1
        fluids[v-1][u-1] = -1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if fluids[i][k] == 1 and fluids[k][j] == 1:
                    fluids[i][j] = 1
                    fluids[j][i] = -1
                elif fluids[i][k] == -1 and fluids[k][j] == -1:
                    fluids[i][j] = -1
                    fluids[j][i] = 1
                # i,j,k -> fluids[x][y] = fluids[x][z] + fluids[z][y]
                #                 i j           i  k           k   j
    for f in fluids:
        cnts = f.count(0)
        if cnts == 1:
            answer += 1
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
sol = solution(n, results)
print(sol)