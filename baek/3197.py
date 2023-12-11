import sys
from collections import deque
input=sys.stdin.readline

y,x=map(int,input().split(' '))
maze=[list(input()[:-1]) for _ in range(y)]
q=deque()
flag=0
move=((-1,0),(1,0),(0,-1),(0,1))#상하좌우
visited=[[0 for _ in range(x)] for _ in range(y)]

def printmaze():
    for i in maze:
        print(i)
        
for yy in range(y):
    for xx in range(x):
        if maze[yy][xx]!="X":
            q.append((yy,xx))
        if maze[yy][xx]=="L" and flag==0:
            starty,startx=yy,xx
            flag=1
            

#flood fill L            
def flood(sy,sx):
    tempq=deque()
    tempq.append((sy,sx))
    while tempq:
        yy,xx=tempq.popleft()
        maze[yy][xx]=0
        visited[yy][xx]=1
        for my,mx in move:
            if yy+my<0 or yy+my>=y or xx+mx<0 or xx+mx>=x:
                continue
            if maze[yy+my][xx+mx]==".":
                tempq.append((yy+my,xx+mx))

newq=deque()      

def search():
    while newq:
        yy,xx=newq.popleft()
        current=maze[yy][xx]#무조건 숫자
        visited[yy][xx]=1
        for my,mx in move:
            if yy+my<0 or yy+my>=y or xx+mx<0 or xx+mx>=x:
                continue
            if maze[yy+my][xx+mx]=="L":
                return current
            if maze[yy+my][xx+mx]==".":
                maze[yy+my][xx+mx]=current
                newq.append((yy+my,xx+mx))
            elif maze[yy+my][xx+mx]!="X" and visited[yy+my][xx+mx]==0:
                newq.append((yy+my,xx+mx))

    return -1

def bfs():
    level=0
    while q:
        yy,xx=q.popleft()
        current=maze[yy][xx]
        if current!=".":
            if current!=level:
                t=search()
                # printmaze()
                # print("-----------------------")
                if t!=-1:
                    return t
                level+=1
        for my,mx in move:
            if yy+my<0 or yy+my>=y or xx+mx<0 or xx+mx>=x:
                continue
            if maze[yy+my][xx+mx]=="X":
                if current=="." or current=="L":
                    maze[yy+my][xx+mx]="."
                else:
                    maze[yy+my][xx+mx]=current+1
                    newq.append((yy+my,xx+mx))
                q.append((yy+my,xx+mx))                  

    
     
flood(starty,startx)
# print("flood")
# printmaze()
answer=bfs()
#print maze
# printmaze()
print(answer)


