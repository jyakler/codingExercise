import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

area = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y):
    current_tree = area[y][x]
    if visited[y][x]:
        return dp[y][x]
    # init
    visited[y][x] = 1
    dp[y][x] = 1

    # move
    for my, mx in mv:
        new_y = my+y
        new_x = mx+x
        if new_y >= n or new_x >= n or new_y < 0 or new_x < 0:
            continue
        if current_tree < area[new_y][new_x]:
            highest_flag = 0
            return_dp = dfs(new_x, new_y)
            dp[y][x] = max(dp[y][x], return_dp+1)
    return dp[y][x]


# calculate
answer = 0
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            answer = max(answer, dfs(x, y))
print(answer)
