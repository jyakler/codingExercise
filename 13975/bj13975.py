import sys

input=sys.stdin.readline
MAX=sys.maxsize

t=int(input())

def insertionsort(arr,key):
    arr.append(key)
    key=arr[-1]
    j=len(arr)-2
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key


def sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

def solve():
    n=int(input())
    file=list(map(int,input().split()))
    sort(file)
    result=0
    newarr=file
    while(len(newarr)>=2):
        sum1=newarr[0]+newarr[1]
        result+=sum1
        newarr=newarr[2:]
        if(len(newarr)!=0):
            insertionsort(newarr,sum1)
    print(result)





for _ in range(t):
    solve()
