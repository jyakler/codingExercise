import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split(' ')))
M=int(input())
mm=list(map(int,input().split(' ')))
l.sort()

    
def binary(array,target):
    s=0
    e=len(array)
    while s<e:
        mid=s+(e-s)//2
        if array[mid]==target:
            return 1
        elif array[mid]<target:
            s=mid+1
        else:
            e=mid
    return 0

for i in mm:
    print(binary(l,i), end=" ")