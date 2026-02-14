from itertools import combinations

def solution(n, q, ans):
    answer = 0
    combs = combinations(range(1, n+1), 5)
    for comb in combs:
        isAnswer = check(q, comb, ans)
        if (isAnswer):
            answer += 1
    return answer

def check(q, comb, ans):
    for i in range(len(q)):
        common = list(set(q[i]) & set(comb))
        if len(common) == ans[i]:
            continue
        else:
            return False
    return True