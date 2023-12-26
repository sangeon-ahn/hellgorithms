import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))


ans = [-sys.maxsize, sys.maxsize]

def 

def backtracking(depth, val):
    global ans
    if depth == N - 1:
        ans[0] = max(ans[0], val)
        ans[1] = min(ans[1], val)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                backtracking(depth + 1, val + A[depth + 1])
            elif i == 1:
                backtracking(depth + 1, val - A[depth + 1])    
            elif i == 2:
                backtracking(depth + 1, val * A[depth + 1])
            else:
                if val < 0:
                    backtracking(depth + 1, -(-val // A[depth + 1]))
                else:
                    backtracking(depth + 1, val // A[depth + 1])
            ops[i] += 1

backtracking(0, A[0])
print(ans)