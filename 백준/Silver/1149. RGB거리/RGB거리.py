import sys
input=sys.stdin.readline

N=int(input())

r=0
g=1
b=2

dp=[[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    dp[i][r],dp[i][g],dp[i][b]=map(int,input().split())

for i in range(1,N):
    max_til_now=[1e9,1e9,1e9]
    for rgb in range(3):
        max_til_now[rgb]=min(max_til_now[rgb],
                             dp[i][rgb]+dp[i-1][(rgb-1)%3],
                             dp[i][rgb]+dp[i-1][(rgb-2)%3])
    dp[i]=max_til_now

print(min(dp[-1]))