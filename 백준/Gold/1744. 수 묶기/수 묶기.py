import sys

input=sys.stdin.readline

N=int(input())
num_list=[int(input()) for _ in range(N)]
plus=[]
minus=[]
zero=[]
for i in num_list:
    if i==0:
        zero.append(i)
    elif i>0:
        plus.append(i)
    else:
        minus.append(i)
    
plus.sort()
minus.sort(reverse=True)

def cal_minus(isZero,minus):
    total=len(minus)
    cnt=0
    if total%2==0:
        left=0
    else:
        left=1
    while len(minus)-left>0:
        a=minus.pop()
        b=minus.pop()
        cnt+=a*b
    if minus:
        left=minus[0]
    if isZero:
        return cnt
    else:
        return cnt+left
    
def cal_plus(plus):
    cnt=0
    while plus:
        try:
            a=plus.pop()
            b=plus.pop()
            cnt+=max(a*b,a+b)
        except:
            cnt+=a
    return cnt

print(cal_plus(plus)+cal_minus(len(zero),minus))