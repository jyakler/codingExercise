import sys
input = sys.stdin.readline
N = int(input())

dp = [[] for _ in range(N+1)]
dp[0] = [-1]
dp[1] = [1]
# dp[2] = [1, 2]
# dp[3] = [1, 3]

for i in range(2, N+1):
    if i % 3 == 0 and i % 2 != 0:
        if len(dp[i//3]) > len(dp[i-1]):
            dp[i] = dp[i-1]+[i]
        else:
            dp[i] = dp[i//3]+[i]
    elif i % 3 != 0 and i % 2 == 0:
        if len(dp[i//2]) > len(dp[i-1]):
            dp[i] = dp[i-1]+[i]
        else:
            dp[i] = dp[i//2]+[i]
    elif i % 3 == 0 and i % 2 == 0:
        if len(dp[i//3]) > len(dp[i//2]):
            dp[i] = dp[i//2]+[i]
        else:
            dp[i] = dp[i//3]+[i]
    else:
        dp[i] = dp[i-1]+[i]

print(len(dp[N])-1)
print(' '.join(list(map(str, reversed(dp[N])))))