import sys
input=sys.stdin.readline
sq,cal=map(int,input().split())
cube=[]
for _ in range(sq):
    cube.append(list(map(int,input().split())))
S=[[0 for _ in range(sq+1)] for _ in range(sq+1)]  

for i in range(1,sq+1):
    for j in range(1,sq+1):
        S[i][j]=S[i-1][j]+S[i][j-1]-S[i-1][j-1]+cube[i-1][j-1]

for _ in range(cal):
    x1,y1,x2,y2=map(int,input().split())
    print(S[x2][y2]-S[x2][y1-1]-S[x1-1][y2]+S[x1-1][y1-1])