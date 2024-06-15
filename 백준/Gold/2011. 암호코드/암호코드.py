# 유효 1~26
d=[0 for _ in range(5002)]
d[0]=1
def sol():
    N=str(input())
    for i in range(len(N)):
        
        if i==0:
            if int(N[i])==0:
                return 0
            d[i+1]=1
            continue
        if 0<int(N[i])<=9:
            # 한자리 수 가능
            d[i+1]+=d[i]
        if 10<=int(N[i-1:i+1])<=26:
            #두자리 수 가능
            d[i+1]+=d[i-1]
        if int(N[i])==0:
            if N[i-1:i+1]!="20" and N[i-1:i+1]!="10":
                return 0
    #     print("current: ",N[i],i,d[i+1])
    # print(d[:10])
    return d[len(N)]
    
print(sol()%1000000)