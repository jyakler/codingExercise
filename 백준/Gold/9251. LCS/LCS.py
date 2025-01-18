import sys
import time
input=sys.stdin.readline

first=input().rstrip()
second=input().rstrip()

dp=[[0] * (len(second)+1) for _ in range(len(first)+1)]


for f in range(1,len(first)+1):
    for s in range(1,len(second)+1):
        if first[f-1]==second[s-1]:
            dp[f][s]=dp[f-1][s-1]+1
        else:
            dp[f][s]=max(dp[f][s-1],dp[f-1][s])


# for i in dp:
#     print(i)
print(dp[-1][-1])