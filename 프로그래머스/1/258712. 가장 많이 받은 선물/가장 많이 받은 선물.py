def solution(friends, gifts):
    answer = 0
    mapp=dict()
    cnt=0
    for i in friends:
        mapp[i]=mapp.get(i,cnt)
        cnt+=1
    N=len(friends)
    l=[[0]*N for _ in range(N)]

    for i in gifts:
        s,r=i.split(' ')
        l[mapp[s]][mapp[r]]+=1
        l[mapp[r]][mapp[s]]-=1
    p=[sum(i) for i in l]
    m=0
    for i in range(N):
        cnt=0
        for j in range(N):
            if i==j or l[i][j]<0: continue
            if l[i][j]>0:
                cnt+=1
            else:
                if p[i]>p[j]:
                    cnt+=1
        m=max(m,cnt)
                
            
    return m