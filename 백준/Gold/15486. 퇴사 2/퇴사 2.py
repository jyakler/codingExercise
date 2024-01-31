import sys
input=sys.stdin.readline

N=int(input())
day=[]
for _ in range(N):
    day.append(list(map(int,input().split())))

dp=[0 for _ in range(N+2)]
start=N
for t,price in day[::-1]:
    if(start+t>N+1):
        dp[start]=dp[start+1]
    elif price>dp[start+1]-dp[start+t]:
            dp[start]=price+dp[start+t]
    else:
        dp[start]=dp[start+1]
    start-=1
print(dp[1])