import sys
from functools import reduce

input = sys.stdin.readline

N, needed = map(int, input().split())
trees = list(map(int, input().split()))
max_height = max(trees)
min_height = 0
H = 0

# binary search
while (True):
    if min_height >= max_height:
        break
    current_h = (min_height+max_height)//2
    # print(f"min : {min_height} / max: {max_height} / h : {current_h} / H: {H}")
    gained = reduce(lambda total, tree: total+max(tree-current_h, 0), trees, 0)
    if gained >= needed:
        H = current_h
        min_height = current_h+1
    else:
        max_height = current_h


print(H)
