# (A**B) % C 구하기
# A**B == A**(B//2) * A**(B//2)임. -> B가 짝수일 경우
# 홀수면 + A 해줘야 함.
# 메모이제이션 + 분할정복
from collections import defaultdict
A, B, C = map(int, input().split())

dic = defaultdict(int)


def expo(num, exp):
    if exp == 0:
        return 1
    
    if exp == 1:
        return num % C

    if exp == 2:
        return num * num % C
    
    if exp % 2 == 0:
        return expo(num, exp // 2)**2 % C
    else:
        return expo(num, exp // 2) ** 2 * num % C

ans = expo(A, B)
print(ans)
    







