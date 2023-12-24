import sys

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

maxNum = -sys.maxsize
minNum = sys.maxsize
vis = [False] * (N + 1)

def recur(order, val):
    global N, maxNum, minNum, vis
    if order == N - 1:
        maxNum = max(maxNum, val)
        minNum = min(minNum, val)
        return


    # 재귀 트리구조에서 각각의 노드들은 연산자이다.
    for j in range(4): # 어떤 연산자를 넣을지 결정
        if ops[j] == 0:
            continue

        ops[j] -= 1
        # 0이면 +
        if j == 0:
            recur(order + 1, val + nums[order + 1])
        # 1이면 -
        elif j == 1:
            recur(order + 1, val - nums[order + 1])
        # 2이면 *
        elif j == 2:
            recur(order + 1, val * nums[order + 1])
        # 3이면 %
        else:
            if val < 0:
                recur(order + 1, -((-val) // nums[order + 1]))
            else:
                recur(order + 1, val // nums[order + 1])
        ops[j] += 1
    
recur(0, nums[0])

print(maxNum)
print(minNum)