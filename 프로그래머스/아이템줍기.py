from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    table=[[-1 for _ in range(102)] for _ in range(102)]
    distance=[[-1 for _ in range(102)] for _ in range(102)]

    #네모 그리기
    for idx,(x1,y1,x2,y2) in enumerate(rectangle):   
        draw(table,x1,y1,x2,y2,idx)
    #내부영역 지우기
    for x1,y1,x2,y2 in rectangle:
        for x in range(x1*2+1,x2*2):
            for y in range(y1*2+1,y2*2):
                table[y][x]=-1
    #follow path
    answer=path(table,distance,characterX*2, characterY*2, itemX*2, itemY*2)
    return answer

# 네모 1,2,3,4 대로 table에 넣고
# 교착지점은 0으로 해서 
# 위 -> 왼오
# 오 -> 위 아래
# 아래 -> 오 왼
# 왼 -> 아래 위
# 위 왼 아래 오
movex=[0,-1,0,1]
movey=[-1,0,1,0]
#문제: 교차점에서 시작하면 위치 파악불가

def path(table,distance,x,y,itemX,itemY):
    q=deque()
    current=table[y][x]
    d=0
    q.append((x,y,d))
    while(q):
        curx,cury,d=q.popleft()
        current=table[cury][curx]
        distance[cury][curx]=d
        if curx==itemX and cury==itemY:
            return d
        d+=0.5
        if current!=0:#교착점이 아니면
            for i in range(4):
                if table[cury+movey[i]][curx+movex[i]]==current or table[cury+movey[i]][curx+movex[i]]==0:
                    if distance[cury+movey[i]][curx+movex[i]]==-1:#이미방문x
                        q.append((curx+movex[i],cury+movey[i],d))
        else:
            for i in range(4):
                if table[cury+movey[i]][curx+movex[i]]!=-1:
                    if distance[cury+movey[i]][curx+movex[i]]==-1:
                        q.append((curx+movex[i],cury+movey[i],d))
                    
            
    return -1
    
         

def draw(table,x1,y1,x2,y2,idx):
    x12=x1*2;x22=x2*2;y12=y1*2;y22=y2*2
    for x in range(x12,x22+1):
        if table[y12][x]!=-1 and table[y12][x]!=idx+1:
            table[y12][x]=0
        else:
            table[y12][x]=idx+1
        if table[y22][x]!=-1 and table[y22][x]!=idx+1:
            table[y22][x]=0
        else:
            table[y22][x]=idx+1
    for y in range(y12,y22+1):
        if table[y][x12]!=-1 and table[y][x12]!=idx+1:
            table[y][x12]=0
        else:
            table[y][x12]=idx+1
        if table[y][x22]!=-1 and table[y][x22]!=idx+1:
            table[y][x22]=0
        else:
            table[y][x22]=idx+1
    return


# from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0
#     table=[[-1 for _ in range(12)] for _ in range(12)]
#     distance=[[-1 for _ in range(12)] for _ in range(12)]

#     #네모 그리기
#     for idx,(x1,y1,x2,y2) in enumerate(rectangle):
#         draw(table,x1,y1,x2,y2,idx)
#     #내부영역 지우기
#     for x1,y1,x2,y2 in rectangle:
#         for x in range(x1+1,x2):
#             for y in range(y1+1,y2):
#                 table[y][x]=-1
#     #follow path
#     answer=path(table,distance,characterX, characterY, itemX, itemY)
#     for i in distance:
#         print(i)
#     return answer

# # 네모 1,2,3,4 대로 table에 넣고
# # 교착지점은 0으로 해서 
# # 위 -> 왼오
# # 오 -> 위 아래
# # 아래 -> 오 왼
# # 왼 -> 아래 위
# # 위 왼 아래 오
# movex=[0,-1,0,1]
# movey=[-1,0,1,0]
# #문제: 교차점에서 시작하면 위치 파악불가
# #해결법: 한번 먼저 dfs로 경로 탐색
# def path(table,distance,x,y,itemX,itemY):
#     q=deque()
#     current=table[y][x]
#     d=0
#     q.append((x,y,d))
#     while(q):
#         curx,cury,d=q.popleft()
#         current=table[cury][curx]
#         distance[cury][curx]=d
#         if curx==itemX and cury==itemY:
#             return d
#         d+=1
#         if current!=0:#교착점이 아니면
#             for i in range(4):
#                 if table[cury+movey[i]][curx+movex[i]]==current or table[cury+movey[i]][curx+movex[i]]==0:
#                     if distance[cury+movey[i]][curx+movex[i]]==-1:#이미방문x
#                         q.append((curx+movex[i],cury+movey[i],d))
#         else:
#             for i in range(4):
#                 if table[cury+movey[i]][curx+movex[i]]!=-1:
#                     if distance[cury+movey[i]][curx+movex[i]]==-1:
#                         q.append((curx+movex[i],cury+movey[i],d))
                    
            
#     return -1
    
         

# def draw(table,x1,y1,x2,y2,idx):
#     for x in range(x1,x2+1):
#         if table[y1][x]!=-1 and table[y1][x]!=idx+1:
#             table[y1][x]=0
#         else:
#             table[y1][x]=idx+1
#         if table[y2][x]!=-1 and table[y2][x]!=idx+1:
#             table[y2][x]=0
#         else:
#             table[y2][x]=idx+1
#     for y in range(y1,y2+1):
#         if table[y][x1]!=-1 and table[y][x1]!=idx+1:
#             table[y][x1]=0
#         else:
#             table[y][x1]=idx+1
#         if table[y][x2]!=-1 and table[y][x2]!=idx+1:
#             table[y][x2]=0
#         else:
#             table[y][x2]=idx+1
#     return


# #거리 계산은 bfs

solution([[1,1,5,7]],1,1,4,7)