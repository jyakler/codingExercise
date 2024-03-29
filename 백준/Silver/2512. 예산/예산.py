import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = list(map(int,readl().split(' ')))
	return N, pos


# 입력받는 부분
N, pos = Input_Data()
total=int(sys.stdin.readline())
pos.sort()
# 여기서부터 작성
def cal(pos,target):
    cnt=0
    for i in pos:
        if i<=target:
            cnt+=i
        else:
            cnt+=target
    return cnt

def bs(pos,N,total):
    start=0
    end=max(pos)+1
    save=0
    while start<end:
        mid=start+(end-start)//2
        result=cal(pos,mid) 
        if result<=total:
            save=mid
            start=mid+1
        else:
            end=mid
    return save
# 출력하는 부분
print(bs(pos,N,total))