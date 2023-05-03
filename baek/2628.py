import sys
input=sys.stdin.readline
def solution():
    width, height=map(int,input().split())
    num=int(input())
    height_list=[0,height]
    width_list=[0,width]
    for _ in range(num):
        #0 - 가로선 (즉 height쪽에 영향)
        #1 - 세로선 (즉 width쪽에 영향)
        line, position=map(int,input().split())
        if line:
            width_list.append(position)
        else:
            height_list.append(position)
    #각 list를 정렬
    height_list.sort()
    width_list.sort()
    height_max=0;width_max=0
    # prev=0
    # for i in range(len(height_list)):
    #     if height_list[i]-prev>height_max:
    #         height_max=height_list[i]-prev
    #     prev=height_list[i]
    i=0
    while height-height_list[i]-height_max>0:
        if height_list[i+1]-height_list[i]>height_max:
            height_max=height_list[i+1]-height_list[i]
        i+=1
    i=0
    while width-width_list[i]-width_max>0:
        if width_list[i+1]-width_list[i]>width_max:
            width_max=width_list[i+1]-width_list[i]
        i+=1
    print(height_max*width_max)
solution()