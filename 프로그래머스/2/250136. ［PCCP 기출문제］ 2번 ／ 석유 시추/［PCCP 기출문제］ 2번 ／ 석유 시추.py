from collections import deque

def solution(land):
    answer = 0
    n=len(land)#y
    m=len(land[0])#x
    t_list=change(n,m,land)
    
    for x in range(m):
        total=set()
        count=0
        for y in range(n):
            total.add(land[y][x])
            
        for i in total:
            count+=t_list[i]
            
        answer=max(answer,count)
    return answer



def change(n,m,land):
    group=2
    t_list=[0,0]
    for y in range(n):
        for x in range(m):
            if land[y][x]==1:
                total=bfs2(y,x,land,n,m,group)
                group+=1
                t_list.append(total)
    return t_list

def bfs2(yy,xx,land,n,m,level):
    move=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    q.append((yy,xx))
    count=0
    while q:
        y,x=q.popleft()
        if land[y][x]!=1:
            continue
        land[y][x]=level
        count+=1
        for my,mx in move:
            if 0<=y+my<n and 0<=x+mx<m:
                if land[y+my][x+mx]==1:
                    q.append((y+my,x+mx))
    return count
                
                
                
                
                
                
# def copy(land):
#     temp=[]
#     for i in land:
#         temp.append([ii for ii in i])
#     return temp        
                
def bfs(target,land,n,m):
    move=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    count=0
    for i in range(n):
        q.append((i,target))
    while q:
        y,x=q.popleft()
        if land[y][x]!=1:
            continue
        land[y][x]=0
        count+=1
        for my,mx in move:
            if 0<=y+my<n and 0<=x+mx<m:
                if land[y+my][x+mx]==1:
                    q.append((y+my,x+mx))
    return count