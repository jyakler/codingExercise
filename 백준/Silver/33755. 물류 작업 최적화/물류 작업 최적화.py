import sys
input = sys.stdin.readline

N = int(input())

A = [0]+list(map(int, input().split()))


right_max = [0]*(N+2)
left_max = [0]*(N+1)
current = 0


# 오른 -> 왼
for i in range(1, N+1):
    left_max[i] = A[i]
    left_max[i] = max(left_max[i-1]+A[i], left_max[i])


for i in range(N, 0, -1):
    right_max[i] = A[i]
    right_max[i] = max(right_max[i+1]+A[i], right_max[i])


for i in range(1, N+1):
    print(right_max[i]-A[i]+left_max[i], end=" ")
