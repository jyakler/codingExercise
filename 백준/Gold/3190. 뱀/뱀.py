import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = []
move = dict()

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)
# init
for _ in range(K):
    apples.append(tuple(map(int, input().split())))
L = int(input())
for _ in range(L):
    x, c = input().split()
    x = int(x)
    move[x] = move.get(x, "")
    move[x] = c


def next_direction(current_direction, next):
    m = [RIGHT, DOWN, LEFT, UP]
    current_index = m.index(current_direction)
    if (next == "D"):
        return m[(current_index+1) % 4]
    elif (next == "L"):
        return m[(current_index-1) % 4]


# 현재 위치
currentx = 0
currenty = 0
snake = deque([(currentx, currenty)])
current_direction = RIGHT
time = 0
# simulation
while (True):
    # print(f"time: {time}/ snake body : ", end=" ")
    # for s in snake:
    #     print(f"{s},", end=" ")
    # print()
    time += 1
    # 이동
    currentx += current_direction[1]
    currenty += current_direction[0]
    # 겹쳤는지
    if ((currentx, currenty) in snake):
        break
    snake.append((currentx, currenty))

    # 방향전환
    if (len(move.get(time, "")) == 1):
        current_direction = next_direction(current_direction, move.get(time))
        # print("next move: ", current_direction)
    # 사과 먹었는지
    if ((currenty+1, currentx+1) not in apples):
        # print(f"{currentx},{currenty} is not apple")
        snake.popleft()
    else:
        apples.pop(apples.index((currenty+1, currentx+1)))

    # 넘어갔는지
    if (currentx >= N or currentx < 0 or currenty >= N or currenty < 0):
        break


print(time)
