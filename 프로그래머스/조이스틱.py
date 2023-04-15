# def solution(name):
#     answer = 0
#     change=[0 if x=="A" else 1 for x in name]
#     current =0
#     while sum(change)!=0:
#         change[current]=0
#         answer+=min((ord(name[current])-65),(ord('Z')-ord(name[current]))+1)
#         current,move=direction(current,change)
#         answer+=move
#     return answer

# def direction(current,change):
#     i=1
#     while i<len(change):
#         if change[(current+i)%len(change)]==1:
#             return (current+i)%len(change),i
#         elif change[(current-i)%len(change)]==1:
#             return (current-i)%len(change),i
#         i+=1
#     return -1,0

"""
그리디인줄알았으나 아무리봐도 dfs로 풀어야할것같음
"""

# def solution(name):
#     change=[0 if x=="A" else 1 for x in name]
#     change[0]=0
#     change2=[0 if x=="A" else 1 for x in name]
#     change2[0]=0
#     answer=min(ord(name[0])-ord('A'),ord('Z')-ord(name[0])+1)
#     if sum(change)==0:
#         return answer
#     right=dfs(1,name,answer+1,1,change)
#     left=dfs(len(name)-1,name,answer+1,0,change2)
#     return min(left,right)

# def dfs(current,name,answer,flag,change):
#     change[current]=0
#     answer+=min(ord(name[current])-ord('A'),ord('Z')-ord(name[current])+1)
#     if sum(change)==0:
#         return answer
#     if flag:
#         result=dfs(current+1,name,answer+1,flag,change)
#     else:
#         result=dfs(current-1,name,answer+1,flag,change)

#     return result
"""
    dfs로 풀어보려했는데 자꾸 특정 케이스에서 에러가남
    한쪽 방향으로만 가는거로 생각했는데 BABAAAAAB 일경우 거꾸로 갈일도 생김
"""
name="JAN"
solution(name)
