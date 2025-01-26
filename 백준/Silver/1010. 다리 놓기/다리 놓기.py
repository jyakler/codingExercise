import sys
# from itertools import combinations

input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    # c=list(combinations(range(M),min(N,M-N)))
    # print(len(c))
    upper=1
    lower=1
    for i in range(1,N+1):
        lower*=i
        upper*=(M-i+1)
    print(int(upper/lower))
    