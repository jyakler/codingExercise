import sys
from collections import deque
input=sys.stdin.readline

y,x=map(int,input().split(' '))
maze=[list(map(int,input()[:-1])) for _ in range(y)]
BIG=10e9
move=((0,1),(0,-1),(1,0),(-1,0))
visited=[[[BIG,BIG] for _ in range(x)] for _ in range(y)] #used, not used

def bfs():
    q=deque()#y,x,level,able to break
    q.append((0,0,1,1))
    while q:
        # print("Q: ",q)
        yy,xx,level,bomb=q.popleft()
        if yy==y-1 and xx== x-1:
            return level
        if level>=visited[yy][xx][bomb]:#이미 이것보다 효율좋은게 있음
            continue
        visited[yy][xx][bomb]=level
        # print("current: ",yy,xx,bomb,visited[yy][xx])
        for i in range(4):
            nyy=yy+move[i][0]
            nxx=xx+move[i][1]
            if 0>nyy or nyy>=y or 0>nxx or nxx>=x:
                continue
            if maze[nyy][nxx]==0:
                q.append((nyy,nxx,level+1,bomb))
            elif maze[nyy][nxx]==1:
                if bomb:
                    q.append((nyy,nxx,level+1,bomb-1))
    return -1

#print maze
# for i in maze:
#     print(i)
    
print(bfs())