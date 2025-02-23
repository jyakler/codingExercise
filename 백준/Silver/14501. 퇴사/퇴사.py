import sys
input=sys.stdin.readline

N=int(input())
day=[]
price=[]
result=[0 for _ in range(N+1)]
for i in range(N):
    d,p=map(int,input().split())
    day.append(d)
    price.append(p)
    
day.append(0)
price.append(0)
for idx in range(N):
    duration=day[idx]
    # print("idx,duration: ",idx,duration)
    if idx+duration>N:
        continue
    if idx!=0:
        result[idx]=max(result[idx],result[idx-1])
    result[idx+duration]=max(result[idx+duration],result[idx]+price[idx])
        
    
print(max(result))