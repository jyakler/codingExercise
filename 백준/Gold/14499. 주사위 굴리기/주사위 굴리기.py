import sys

input=sys.stdin.readline

N,M,x,y,K=list(map(int,input().split()))
dice=[0,0,0,0,0,0]
maze=[list(map(int,input().split())) for _ in range(N)]
step=list(map(int,input().split()))
moving=[(0,1),(0,-1),(-1,0),(1,0)]
def turn(dice,move):
    top,left,right,bottom,front,back=dice
    if move==1:#동
        dice=[left,bottom,top,right,front,back]
    elif move==2:#서
        dice=[right,top,bottom,left,front,back]
    elif move==3:#북
        dice=[front,left,right,back,bottom,top]
    else:#남
        dice=[back,left,right,front,top,bottom]
    return dice

# for i in maze:
#     print(i)
# print('----------')
for i in range(K):
    move=step[i]
    my,mx=moving[move-1]
    if (0<=x+my<N and 0<=y+mx<M)==False:
        continue
    
    dice=turn(dice,move)
    print(dice[0])
    current=maze[x+my][y+mx]
    if current==0:
        maze[x+my][y+mx]=dice[3]
    else:
        dice[3]=maze[x+my][y+mx]
        maze[x+my][y+mx]=0
    x+=my
    y+=mx