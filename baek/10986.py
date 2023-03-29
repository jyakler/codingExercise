import sys
input=sys.stdin.readline

#구간합?
# 처음 입력받을때 구간합한뒤 %3 해놓고 
number,divisor=map(int,input().split())
all_num=list(map(int,input().split()))
S=[0 for _ in range(number)]
S[0]=all_num[0]
for i in range(1,number):
    S[i]=S[i-1]+all_num[i]
divided_S=[s%divisor for s in S]

count_num=dict()
for v in divided_S:
    count_num[v]=count_num.get(v,0)+1
    
result=count_num.get(0,0)
for k,v in count_num.items():
    result+=(v*(v-1))//2
print(result)
