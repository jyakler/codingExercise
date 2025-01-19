import sys

input=sys.stdin.readline
N,M=map(int,input().split())
table=[]
dp=[]
dp2=[]
for i in range(N):
    table.append([0]+list(map(int,input().split())))
    
table.insert(0,[0]*(len(table[0])))
for i in table:
    dp.append(([j for j in i]))
    dp2.append(([j for j in i]))


for y in range(1,len(dp)):
    for x in range(1,len(dp[0])):
        dp[y][x]+=dp[y][x-1]

for y in range(1,len(dp)):
    for x in range(1,len(dp[0])):
        dp[y][x]+=dp[y-1][x]

# for i in dp:
#     print(i)    
# print()
 

def calc(x1,x2,y1,y2,dp):
    return dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]


# for i in table:
#     print(i)  
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    # print("result: ",x1,x2,y1,y2)
    print(calc(x1,x2,y1,y2,dp))
    
    

