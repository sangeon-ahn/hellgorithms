import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
items = [list(map(int, input().rstrip().split())) for _ in range(N)]

"""
dp[i]: 무게 i일 때, 최대 가치합
dp[i] = max(dp[i], dp[i-아이템무게] + 아이템가치)
6 13
4 8
3 6
5 12
"""
dp = [0] * (K + 1)

for item in items: 
    for weight in range(K, item[0] - 1, -1):
        if weight >= item[0]:
            dp[weight] = max(dp[weight], dp[weight - item[0]] + item[1])

ans = 0
for i in range(len(dp)):
    if dp[i] > ans:
        ans = dp[i]

print(ans)

