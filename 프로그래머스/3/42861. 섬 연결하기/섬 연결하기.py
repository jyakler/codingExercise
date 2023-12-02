def solution(n, costs):
    costs=sorted(costs,key=lambda x: x[2])
    visited=[i for i in range(n)]
    answer=0
    for s,e,c in costs:
        if find(s,visited)!=find(e,visited):
            answer+=c
            visited[find(e,visited)]=s
    return answer

def find(num,visited):
    while visited[num]!=num:
        num=visited[num]
    return num