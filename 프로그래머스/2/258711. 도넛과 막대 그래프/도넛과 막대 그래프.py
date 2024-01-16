def solution(edges):
    answer = []
    big_d=dict()
    for s,e in edges:
        big_d[s]=big_d.get(s,[0,0])
        big_d[e]=big_d.get(e,[0,0])
        big_d[s][0]+=1
        big_d[e][1]+=1
    big_d=sorted(big_d.items(),key=lambda x:x[1],reverse=True)
    edge=0
    origin=big_d[0][0]
    total=big_d[0][1][0]
    big_d=dict()
    for s,e in edges:
        big_d[e]=big_d.get(e,[0,0])
        if s==origin:
            continue
        big_d[s]=big_d.get(s,[0,0])
        big_d[s][0]+=1
        big_d[e][1]+=1
        edge+=1
    a=0
    b=0
    c=0
    for (start,end) in big_d.values():
        if start==0:
            b+=1
        if start==2 and end==2:
            c+=1
        if end==0:
            b+=1

    # print(big_d)
    # node=len(big_d)
    # print(node,edge)
    # print(node-b,edge-(b-1))
    # print(a,b/2,c)
    
    return [origin,total-b/2-c,b/2,c]