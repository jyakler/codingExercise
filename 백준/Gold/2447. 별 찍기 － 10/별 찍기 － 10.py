import sys

input=sys.stdin.readline

N=int(input())

def star(num):
    if num==1:
        return["*"]
    ans=[]
    s=star(num//3)
    for i in s:
        ans.append(i*3)
    for i in s:
        ans.append(i+" "*(num//3)+i)
    for i in s:
        ans.append(i*3)
    return ans
print('\n'.join(star(N)))

