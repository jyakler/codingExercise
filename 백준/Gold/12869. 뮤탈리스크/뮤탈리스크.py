import sys
input=sys.stdin.readline
dp=[[[0 for _ in range(61)]for _ in range(61)]for _ in range(61)]
def func(x,y,z):
    if(x<0):x=0
    if(y<0):y=0
    if(z<0):z=0
    if (x==y==z==0):
        return 0
    if(dp[x][y][z]>0):return dp[x][y][z]
    dp[x][y][z]=min([func(x-9,y-3,z-1),func(x-9,y-1,z-3),func(x-3,y-1,z-9),func(x-3,y-9,z-1),func(x-1,y-3,z-9),func(x-1,y-9,z-3)])+1
    return dp[x][y][z]

N=int(input())
scvs=[0,0,0]
t=list(map(int,input().split()))
for i in range(len(t)):
    scvs[i]=t[i]
print(func(scvs[0],scvs[1],scvs[2]))