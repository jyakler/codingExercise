import sys

input=sys.stdin.readline
maze=[list(map(int,input().split(' '))) for _ in range(10)]

d=dict()
for i in range(1,6):
    d[i]=d.get(i,5)
def pm():
    print("---------------------------")
    for i in maze:
        print(i)
    print("---------------------------")
    
def find(y,x,num):
    if y+num>10 or x+num>10:
        return 0
    for yy in range(y,y+num):
        for xx in range(x,x+num):
            if maze[yy][xx]!=1:
                return 0
    if d[num]==0:
        return 0
    d[num]-=1
    # print("found ",num,y,x,d[num])
    for yy in range(y,y+num):
        for xx in range(x,x+num):
            maze[yy][xx]=0
    # pm()
    return 1

def sol():
    s=0
    for i in range(5,0,-1):
        for y in range(10):
            for x in range(10):
                if maze[y][x]==1:
                    ans=find(y,x,i)
                    s+=ans
    for y in range(10):
        for x in range(10):
            if maze[y][x]==1:
                print(-1)
                return
    print(s)
sol()