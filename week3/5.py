import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    coins = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for money in range(M, 0, -1):
            cnts = 1
            while coin * cnts <= money:
                dp[money] += dp[money - coin * cnts]
                cnts += 1
                
    print(dp[M])





