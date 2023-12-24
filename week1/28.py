N = int(input())

# 결국, 라인1의 맨 밑 원판을 라인3으로 옮기려면, 맨 밑 원판 위의 원기둥을 라인2로 옮겨야 한다.
# 따라서, 원기둥을 라인2로 옮기고, 맨 밑 원판을 라인3으로 옮기고, 다시 원기둥을 라인3으로 옮기는 작업이 필수적이다.
ans = 0
process = []
def hanoi(x, y, n): # x번째 라인의 크기 n의 원기둥을 y번째 라인으로 옮기고 싶다.
    global ans
    # 크기 1이면 그냥 옮기기
    if n == 1:
        ans += 1
        if N <= 20:
            process.append(f"{x} {y}")

        return
    
    # 크기 2이상이면, x->y 하기 위해서는 z에다가 위에껄 다 옮겨야 한다.
    hanoi(x, 6 - x - y, n - 1) # 다 옮기고,

    if N <= 20:
        process.append(f"{x} {y}")
    ans += 1
    # z->y로 옮기기
    hanoi(6 - x - y, y, n - 1)


print(2**N - 1)
if N <= 20:
    hanoi(1, 3, N)
    for i in range(len(process)):
        print(process[i])

    
