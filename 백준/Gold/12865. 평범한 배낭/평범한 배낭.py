import sys
input=sys.stdin.readline
W=[0]
V=[0]
N,K=map(int,input().split())
dp=[[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    weight,value=map(int,input().split())
    W.append(weight)
    V.append(value)
    
for i in range(1,N+1):
    for w in range(1,K+1):
        left=w-W[i]
        if left<0:
            dp[i][w]=dp[i-1][w]
        else:
            dp[i][w]=max(dp[i-1][left]+V[i],dp[i-1][w])
        
        
# for i in dp:
#     print(i)
print(dp[-1][-1])