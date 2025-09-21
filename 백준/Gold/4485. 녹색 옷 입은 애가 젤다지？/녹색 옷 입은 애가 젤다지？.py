import sys
from collections import deque
import copy
import heapq

input = sys.stdin.readline
INF = 1e9
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down,up,right,left


def dijkstra(N, maze):
    visited = [[0 for _ in range(N)]for _ in range(N)]
    distance = [[INF for _ in range(N)]for _ in range(N)]
    x = 0
    y = 0
    distance[y][x] = maze[y][x]
    min_heap = [(distance[y][x], x, y)]
    heapq.heapify(min_heap)
    while len(min_heap) > 0:
        _, x, y = heapq.heappop(min_heap)
        if visited[y][x]:
            continue
        visited[y][x] = 1
        for move_y, move_x in move:
            new_y = move_y+y
            new_x = move_x+x
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                continue
            if distance[new_y][new_x] > distance[y][x]+maze[new_y][new_x]:
                # 갱신
                distance[new_y][new_x] = distance[y][x]+maze[new_y][new_x]
                heapq.heappush(
                    min_heap, (distance[new_y][new_x], new_x, new_y))
    return distance[-1][-1]


problem = 0
while True:
    problem += 1
    maze_size = int(input())
    if maze_size == 0:
        break
    maze = []
    for _ in range(maze_size):
        maze.append(list(map(int, input().split())))
    answer = dijkstra(maze_size, maze)
    print(f"Problem {problem}: {answer}")
