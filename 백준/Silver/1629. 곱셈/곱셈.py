import sys
import math
sys.setrecursionlimit(10000)
input=sys.stdin.readline

A,B,C=map(int,input().split())

def func(over:int)->int:
    if over==1:
        return A%C
    else:
        a=func(over//2)%C
        if over%2==0:
            # 짝수
            return (a*a)%C
        else:
            return ((a*a)%C)*(A%C)
    
print(func(B)%C)