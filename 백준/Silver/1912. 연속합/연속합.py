import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
current = 0
save = 0
result = -10000
for i in l:
    current += i
    if current > 0 and current > i:
        # 0보다 크면 일단 keep going
        save = current
    else:
        save = i
        current = i
    result = max(result, current, i)
    # print(f"[{i}]: {save}, result:{result}")

print(result)
