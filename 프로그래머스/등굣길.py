m=4
n=3
puddles=[[2,3]]
# def solution(m, n, puddles):
#     answer = 0
#     mapp=[[0 for _ in range(n+1)] for _ in range(m+1)]
#     mapp[1][1]=1
#     for x,y in puddles:
#         mapp[x][y]=-1
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if mapp[i][j]!=0:
#                 continue
#             print(mapp[i-1][j],"+",mapp[i][j-1])
#             mapp[i][j]=max(0,mapp[i-1][j])+max(0,mapp[i][j-1])
#     return mapp[m][n]
"""
위에꺼 구현해보고 print찍어보니 x,y축 거꾸로 진행한거였음
근데 이건 왜 맞고 아래는 틀리나했더니 puddle도 거꾸로 넣어야했었음.
위 문제는 효율성이 틀린데 이유는 1,000,000,007 나머지를 return 하지 않아서.
    
"""


def solution(m, n, puddles):
    answer = 0
    mapp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    mapp[1][1]=1
    for x,y in puddles:
        mapp[y][x]=-1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if mapp[i][j]!=0:
                continue
            mapp[i][j]=max(0,mapp[i-1][j])+max(0,mapp[i][j-1])
    for i in mapp:
        print(i)
    return mapp[n][m]%1000000007




solution(m,n,puddles)