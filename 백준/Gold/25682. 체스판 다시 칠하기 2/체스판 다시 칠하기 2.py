import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
maze = [input().strip() for _ in range(N)]

def get_min_paint(color_to_start):
    # 누적합 배열 초기화 (N+1 x M+1)
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            paint = 0
            # (i+j)가 짝수이면 시작색과 같아야 함, 홀수이면 달라야 함
            if (i + j) % 2 == 0:
                if maze[i-1][j-1] != color_to_start:
                    paint = 1
            else:
                if maze[i-1][j-1] == color_to_start:
                    paint = 1
            
            # 2차원 누적합 공식
            prefix_sum[i][j] = paint + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    
    # KxK 구간합 중 최솟값 찾기
    min_val = float('inf')
    for i in range(K, N + 1):
        for j in range(K, M + 1):
            count = prefix_sum[i][j] - prefix_sum[i-K][j] - prefix_sum[i][j-K] + prefix_sum[i-K][j-K]
            if count < min_val:
                min_val = count
    return min_val

# 'W'로 시작하는 경우와 'B'로 시작하는 경우 중 최솟값 출력
print(min(get_min_paint('W'), get_min_paint('B')))