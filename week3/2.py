import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0] * (N + 10) # dp[i]: N = i일 때 만들 수 있는 2진수 개수
# dp[i] = dp[i-1] + dp[i-2]

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])