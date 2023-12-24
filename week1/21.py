N = int(input())
nums = list(map(int, input().split()))

def eratos(size):
    result = [True for _ in range(size + 1)]
    result[0] = False
    result[1] = False

    for i in range(2, size + 1):
        # 이미 소수가 아니라고 체크했으면 해당 수의 배수 역시 체크가 되었을 것이므로 패스.
        if not result[i]:
            continue

        for j in range(i*i, size + 1, i):
            result[j] = False
    
    return result

isSosu = eratos(1000)

ans = 0
for n in nums:
    if isSosu[n]:
        ans += 1

print(ans)

    





