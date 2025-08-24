import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def printf(x):
    if isinstance(x, list):
        for i in x:
            print(i)
    else:
        print(x)


move = [(0, 1), (1, 0), (1, 1)]
maze = []
maze.append([0 for _ in range(M+2)])
for i in range(N):
    maze.append([0]+list(map(int, input().split()))+[0])
maze.append([0 for _ in range(M+2)])


def sol():
    for i in range(1, N+1):
        for j in range(1, M+1):
            maze[i][j] = maze[i][j] + \
                max(maze[i-1][j-1], maze[i-1][j], maze[i][j-1])
    pass


# print()
sol()
m = 0
for i in maze:
    if m < max(i):
        m = max(i)
print(m)
