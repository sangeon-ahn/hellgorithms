import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

"""
dp[i][j]: str1은 i번째까지, str2는 j번째까지의 수열을 봤을 때, 최장 공통 부분수열의 길이
dp[i][j] = max(dp[i-1][j], dp[i-1][j])
"""

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

# for i in range(len(dp)):
#     print(dp[i])

print(dp[len(s2)][len(s1)])