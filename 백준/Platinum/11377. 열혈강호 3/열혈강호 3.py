import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

employee = dict()
jobs = dict()
# init
for i in range(N):
    canDo = list(map(int, input().split()))
    employee[i+1] = employee.get(i+1, canDo[1:])

who_visited = [-1 for _ in range(M+1)]


def matching(employee_number):
    for target in employee[employee_number]:
        if visited[target]:
            continue
        visited[target] = True

        if who_visited[target] == -1:
            who_visited[target] = employee_number
            return True
        else:
            flag = matching(who_visited[target])
            if flag:
                who_visited[target] = employee_number
                return True
    return False


count = 0
for i in range(1, N+1):
    visited = [False for _ in range(M+1)]  # 중복탐색
    if matching(i):
        count += 1

# K 처리
k_count = 0
for i in range(1, N+1):
    if k_count == K:
        break
    visited = [False for _ in range(M+1)]  # 중복탐색
    if matching(i):
        k_count += 1
        count += 1
print(count)
