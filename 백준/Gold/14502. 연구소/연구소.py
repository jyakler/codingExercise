import sys
from itertools import combinations
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = []
maze.append([1 for _ in range(M+2)])
for _ in range(N):
    maze.append([1]+list(map(int, input().split()))+[1])
maze.append([1 for _ in range(M+2)])

empty = []
virus = []
for y in range(1, N+1):
    for x in range(1, M+1):
        if maze[y][x] == 2:
            virus.append((x, y))
        elif maze[y][x] == 0:
            empty.append((x, y))

combs = combinations(empty, 3)

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_safe = 0

for comb in combs:
    # 초기화
    new_maze = copy.deepcopy(maze)
    virusq = deque()
    for i in virus:
        virusq.append(i)

    # 추가 벽
    for wallx, wally in comb:
        new_maze[wally][wallx] = 1

    while len(virusq) > 0:
        startx, starty = virusq.popleft()
        for mx, my in move:
            if new_maze[starty+my][startx+mx] == 0:
                new_maze[starty+my][startx+mx] = 2
                virusq.append((startx+mx, starty+my))

    total_safe = 0
    for i in new_maze:
        total_safe += i.count(0)

    # for i in new_maze:
    #     print(i)
    # print(f"current safe: {total_safe}\n========\n")
    max_safe = max(max_safe, total_safe)


print(max_safe)
