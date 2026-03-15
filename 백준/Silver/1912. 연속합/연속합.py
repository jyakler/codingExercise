import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
dp = [0] * 100001
result = -100000
for i in range(1, n+1):
    dp[i] = max(dp[i-1]+l[i-1], l[i-1])
    result = max(result, dp[i])
print(result)
