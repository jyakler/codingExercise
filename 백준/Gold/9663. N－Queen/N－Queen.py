import sys

input = sys.stdin.readline

N = int(input())

queen = []
x, y = 0, 0
result = 0
blockx = []
blocky = []
blockds = []
blockda = []
queen = []


def dfs(x, blocky, blockds, blockda, level, queen):
    global result
    if level == N:
        result += 1
        return
    for y in range(N):
        if y in blocky or x-y in blockds or x+y in blockda:
            continue
        blocky.append(y)
        blockds.append(x-y)
        blockda.append(x+y)
        queen.append((x, y))
        dfs(x+1, blocky, blockds, blockda, level+1, queen)
        blocky.pop()
        blockds.pop()
        blockda.pop()
        queen.pop()


dfs(0, blocky, blockds, blockda, 0, queen)
print(result)
