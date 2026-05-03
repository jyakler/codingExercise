from itertools import combinations

def solution(n, q, ans):
    answer = 0
    combs = combinations(range(1,n+1),5)
    for comb in combs:
        answer+=check(comb,q,ans)
    return answer


def check(comb,q,ans):
    for i in range(len(ans)):
        target=0
        for qq in q[i]:
            if qq in comb:
                target+=1
        if target!=ans[i]:
            return 0
    return 1
        