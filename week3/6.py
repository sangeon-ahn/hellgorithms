import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = list(set([int(input().rstrip()) for _ in range(n)]))

dp = [sys.maxsize] * (k + 1)
dp[0] = 0

for coin in coins:
    for money in range(coin, k + 1):
        dp[money] = min(dp[money], dp[money - coin] + 1)


if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
