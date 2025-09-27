def load():
    # 첫째 줄에서 수열의 크기 N을 입력받습니다.
    N, M = list(map(int, input().split()))

    # N개의 수열을 입력받습니다.
    sequences = []
    for _ in range(N):
        num = list(map(int, input().split()))
        sequences.append(num)

    # 입력된 수열 출력 (테스트용)
    # print("입력된 수열:", sequences)

    return N,M, sequences

def make_walls(N,M,sequences):

    from itertools import combinations

    points = []
    virus = []

    for i in range(N):
        for j in range(M):
            if sequences[i][j] == 0 :

                points.append((i,j))
            
            elif sequences[i][j] == 2 :
                virus.append((i,j))

    
    combs = list(combinations(points, 3))

    return len(points)-3, virus , combs




def bfs(N, M, virus, sequences):

    from collections import deque

    rs = 0


    visited = [[ 0 for _ in range(M) ] for _ in range(N)]


    queue = deque(virus)

    move = [(1,0),(0,1),(-1,0),(0,-1)]


    while queue:

        q = queue.popleft()

        x,y = q

        visited[x][y] = 1

        for m in move:
            nX = x+m[0]
            nY = y+m[1]


            if (0 <= nX < N) and (0 <= nY < M):

                if (visited[nX][nY] != 1):

                    if (sequences[nX][nY] == 0):
                        visited[nX][nY] = 1
                        queue.append((nX,nY))
                        rs += 1

    return rs

def main():
    import copy
    N,M, sequences = load()

    answer = 0

    spaces,virus, wall_points = make_walls(N=N, M=M, sequences=sequences)

    for walls in wall_points:
        new_sequences = copy.deepcopy(sequences)
        
        for wall in walls:
            new_sequences[wall[0]][wall[1]] = 1

        rs = bfs(N,M, virus, new_sequences)

        rest = (spaces - rs)

        if rest >= answer:
            answer = rest

    print(answer)

if __name__ == "__main__":
    main()

"""[
[2, 1, 0, 0, 1, 1, 2], 
[1, 0, 1, 0, 1, 2, 2], 
[0, 1, 1, 0, 1, 2, 2], 
[0, 1, 0, 0, 0, 1, 2], 
[0, 0, 0, 0, 0, 1, 1], 
[0, 1, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0]]"""

"""[[2, 1, 0, 0, 1, 1, 2], 
[1, 0, 1, 0, 1, 2, 2], 
[0, 1, 1, 0, 1, 2, 2], 
[0, 1, 0, 0, 0, 1, 2], 
[0, 0, 0, 0, 0, 1, 1], 
[0, 1, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0]]"""