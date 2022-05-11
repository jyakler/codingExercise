import sys
import heapq
input=sys.stdin.readline
MAX=sys.maxsize

t=int(input())

def solve():
    n=int(input())
    file=list(map(int,input().split()))
    result=0
    arr=[]
    for i in file:
        heapq.heappush(arr,i)
    while(len(arr)>1):
        a=heapq.heappop(arr)
        b=heapq.heappop(arr)
        result+=a+b
        heapq.heappush(arr,a+b)
    print(result)

for _ in range(t):
    solve()
