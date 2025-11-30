import sys

input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(2)]

# 0 - 연속x , 1- 연속o
dp[0][0] = wine[0]
dp[1][0] = wine[0]

if (N >= 2):
    dp[0][1] = wine[1]
    dp[1][1] = dp[0][0]+wine[1]

if (N >= 3):
    dp[0][2] = dp[0][0]+wine[2]
    dp[1][2] = max(dp[0][1]+wine[2], dp[1][1])

# dp[0][3] = max(dp[1][3-2], dp[0][3-2])+wine[3]  / max(dp[1][3-3],dp[0][3-1])
# dp[1][3] = dp[0][3-1]+wine[3]

# print(f"dp {0}: {dp[0][0]} / {dp[1][0]}")
# print(f"dp {1}: {dp[0][1]} / {dp[1][1]}")
# print(f"dp {2}: {dp[0][2]} / {dp[1][2]}")
for i in range(3, N):
    dp[0][i] = max(dp[1][i-2], dp[0][i-2])+wine[i]
    dp[1][i] = max(dp[0][i-1]+wine[i], dp[1][i-1])
    # print(f"dp {i}: {dp[0][i]} / {dp[1][i]}")

print(max(max(dp[0]), max(dp[1])))
