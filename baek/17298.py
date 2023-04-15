"""
    코테 보다가 이거랑 비슷한 문제가 나와서 시험에서 못본김에 공부할겸 풀어봄.
    시험때는 똑같이 append하고 비교하면서 했는데 timeout떴는데 그때는 순방향(-1이아니라)부터 비교해서 그런것같음 ㅜㅜ
"""

import sys
readl=sys.stdin.readline
num=int(readl())
x=list(map(int,readl().split()))
INF=1000001
answer=[-1 for _ in range(num)]
minnum=INF
stack=[]
for i in range(len(x)):
    while stack and x[stack[-1]]<=x[i]:
        answer[stack.pop()]=x[i]
    stack.append(i)

print(*answer)