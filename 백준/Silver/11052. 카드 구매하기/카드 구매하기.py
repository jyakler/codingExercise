import sys
input = sys.stdin.readline

N = int(input())
P = [0]+list(map(int, input().split()))
max_price = 0
dp = [0 for _ in range(N+1)]

# dp
def dp_buy():
    dp[1] = P[1]
    dp[2] = max(dp[1]*2, P[2])
    for i in range(3, N+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i-j]+dp[j], P[i], dp[i])
            # print("J: ", j, "dp[", i, "]= ", dp[i])


dp_buy()
print(dp[N])
