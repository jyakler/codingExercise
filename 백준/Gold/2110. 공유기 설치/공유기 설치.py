import sys
input=sys.stdin.readline

N,C=map(int,input().split(' '))
l=[int(input()) for _ in range(N)]
l.sort()

def bin(array,C):
    start=1 # 거리 최소
    end=l[-1]-l[0] #거리 최대
    ans=0
    if C==2:
        return end
    while start<end:
        current=array[0]
        count=1
        mid=start+(end-start)//2
        # print("----------")
        # print("mid,start,end: ",mid,start,end)
        # print(current,end=" ")
        for i in range(1,len(array)):
            if array[i]>=current+mid:
                current=array[i]
                # print(current, end=" ")
                count+=1
        # if count==C:
        #     return mid
        if count>=C:
            ans=mid
            start=mid+1
        else:
            end=mid
    return ans

print(bin(l,C))
