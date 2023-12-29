import sys
from collections import deque

input=sys.stdin.readline
move=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
M,N,H=map(int,input().split(' '))
cage=[[[i for i in map(int,input().split(' '))] for _ in range(N)] for _ in range(H)]
q=deque()

for h in range(H):
    for y in range(N):
        for x in range(M):
            if cage[h][y][x]==1:
                q.append((h,y,x,1))#h,y,x,level
level=1
while q:
    h,y,x,level=q.popleft()
    for mh,my,mx in move:
        if not (0<=h+mh<H and 0<=y+my<N and 0<=x+mx<M):
            continue
        if cage[mh+h][my+y][mx+x]==0:
            cage[mh+h][my+y][mx+x]=level+1
            q.append((mh+h,my+y,mx+x,level+1))

answer=level-1
for i in cage:
    for ii in i:
        for iii in ii:
            if iii==0:
                answer=-1
print(answer)

