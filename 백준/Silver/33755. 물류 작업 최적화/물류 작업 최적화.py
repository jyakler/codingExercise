import sys
input = sys.stdin.readline

N = int(input())

A = [0]+list(map(int, input().split()))


right_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
left_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
current = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        right_sum[i][j] = right_sum[i][j-1]+A[j]


for i in range(N, 0, -1):
    for j in range(i-1, 0, -1):
        left_sum[i][j] = left_sum[i][j+1]+A[j]

for i in range(1, N+1):
    print(max(right_sum[i])+A[i]+max(left_sum[i]), end=" ")
