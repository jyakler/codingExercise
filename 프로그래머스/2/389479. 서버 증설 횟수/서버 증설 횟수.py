import math

def solution(players, m, k):
    answer = 0
    server = [0 for _ in range(len(players))]
    length = len(players)
    for i in range(length):
        if players[i]<m:
            continue
        if players[i]>=server[i]*m and players[i]<(server[i]+1)*m:
            continue
        
        need_server=players[i]//m
        added_server=max(need_server-server[i],0)
        answer+=added_server
        for ii in range(i,min(length,i+k)):
            server[ii]+=added_server
    # print(server)
    return answer