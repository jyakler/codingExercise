import sys

def input_data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    shoots.sort()
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals


sol = 0

# 입력받는 부분
#사대 동물 사정거리
M, N, L, shoots, animals = input_data()
def low(x,y,l,shoots):
    s,e=0,len(shoots)
    while s<e:
        #아래에서 올라옴
        mid=s+(e-s)//2
        dis=abs(x-shoots[mid])+y
        if dis<=l:
            return 1
        else:
            e=mid
    s,e=0,len(shoots)
    while s<e:
        #위에서 내려옴
        mid=s+(e-s)//2
        dis=abs(x-shoots[mid])+y
        if dis<=l:
            return 1
        else:
            s=mid+1
    return 0

# 여기서부터 작성
for x,y in animals:
    sol+=low(x,y,L,shoots)
    

# 출력받는 부분
print(sol)