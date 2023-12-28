import sys
input = sys.stdin.readline

T = int(input().rstrip()) # 만들어야 하는 금액
k = int(input().rstrip()) # 동전 가치의 종류
coins = [list(map(int, input().rstrip().split())) for _ in range(k)] # 동전 가치 별 개수
coins.sort(key = lambda coin : coin[0])
# dp[money] = dp[money - k] + 1, money: 만들어야 할 금액, k: 현재 보고있는 동전 가치, dp[i] = 금액 i를 만들 수 있는 동전 조합 가지수.
dp = [0] * (T + 1)
dp[0] = 1

for coin, cnt in coins: # 1, 5, 10원
    for money in range(T, 0, -1):
        for i in range(1, cnt + 1):
            if money < i * coin:
                break

            dp[money] += dp[money - coin * i]

print(dp[-1])
