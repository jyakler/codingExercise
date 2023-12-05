def solution(tickets):
    answer = []
    d=dict()
    tickets=sorted(tickets)
    l=[]
    for i in tickets:
        l.extend(i)
    for i in l:
        d[i]=d.get(i,[])

    for start,end in tickets:
        d[start]=d.get(start,[])
        d[start].append(end)
    answer=dfs("ICN",d,["ICN"],len(tickets)+1)
    return answer



def dfs(current,ticket_d,stack,total):
    # print(current,ticket_d)
    t=ticket_d[current].copy()
    # print(t)
    for i in t:
        stack.append(i)
        ticket_d[current].remove(i)
        if len(stack)==total:
            return stack
        result=dfs(i,ticket_d,stack,total)

        if result!=-1:
            return result
        ticket_d[current].append(i)
        stack.pop()
    return -1