N = int(input())

# visited 배열들
garos = [False] * (N + 1)
seros = [False] * (N + 1)
diagonal1 = [False] * (2 * N)
diagonal2 = [False] * (2 * N)
ans = 0

def check(x, y):
    if not (garos[x] or seros[y] or diagonal1[x - y] or diagonal2[x + y]):
        return True
    return False

def backtracking(order, n):
    global ans
    if order == n:
        ans += 1
        return
    
    for i in range(n):
        if garos[i] or seros[order] or diagonal1[i - order] or diagonal2[i + order]:
            continue

        garos[i] = True
        seros[order] = True
        diagonal1[i - order] = True
        diagonal2[i + order] = True
        backtracking(order + 1, n)
        garos[i] = False
        seros[order] = False
        diagonal1[i - order] = False
        diagonal2[i + order] = False

backtracking(0, N)
print(ans)
# y = x - 1, y = x + 1
# x - y = -1, x - y = 1
# x - y = 0, x + y = 2
