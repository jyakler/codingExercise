import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = dict()
for i in range(N+1):
    dp[i] = dp.get(i, set())

dp[0].add(S)
for i in range(1, N+1):
    for before in dp[i-1]:
        if (before-V[i-1] >= 0):
            dp[i].add(before-V[i-1])
        if before+V[i-1] <= M:
            dp[i].add(before+V[i-1])

if(len(dp[N])==0): print(-1)
else: print(max(dp[N]))
