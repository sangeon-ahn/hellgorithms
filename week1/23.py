N = int(input())
answer = 0

def isHansu(num):
    numStr = str(num)

    # 차이를 구한다.
    diff = int(numStr[0]) - int(numStr[1])

    # for 문 돌면서 차이가 diff와 같지 않으면 False
    
    for i in range(1, len(numStr) - 1):
        if int(numStr[i]) - int(numStr[i + 1]) != diff:
            return False
    
    return True

for i in range(1, N + 1):
    # 100 이하면 한수다.
    if i < 100:
        answer += 1
        continue


    if isHansu(i):
        answer += 1

print(answer)
