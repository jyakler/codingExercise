import sys
sys.setrecursionlimit(int(1e9))
input=sys.stdin.readline

N=int(input())

total=list(map(int,input().split(' ')))
M=int(input())

select=list(map(int,input().split(' ')))

d=dict()
for i in total:
    d[i]=d.get(i,0)+1
    
for i in select:
    if i not in d:
        print(0,end=" ")
    else:
        print(d[i],end=" ")