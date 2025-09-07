import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
first = input().strip()
second = input().strip()
dp = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

stack = []


def sol():
    for i in range(1, len(first)+1):
        for j in range(1, len(second)+1):
            if first[i-1] == second[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])


sol()

i = len(first)
j = len(second)
while i >= 1 and j >= 1:
    current = dp[i][j]
    up = dp[i-1][j]
    left = dp[i][j-1]
    dae = dp[i-1][j-1]
    if current > max(up, left, dae):
        # 현재 값기준 바뀌었음
        stack.append(first[i-1])
        i -= 1
        j -= 1
    else:
        if dae == current:
            i -= 1
            j -= 1
        elif current == left:
            j -= 1
        else:
            i -= 1
print(dp[-1][-1])
print(''.join(stack[::-1]))
