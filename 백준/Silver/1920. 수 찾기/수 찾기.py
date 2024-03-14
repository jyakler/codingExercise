import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split(' ')))
M=int(input())
ll=list(map(int,input().split(' ')))
l.sort()

def bin(array,target):
    s,e=0,len(array)
    while s<e:
        mid=s+(e-s)//2
        if array[mid]==target:
            return 1
        elif array[mid]<target:
            s=mid+1
        else:
            e=mid
    return 0

for i in ll:
    print(bin(l,i))