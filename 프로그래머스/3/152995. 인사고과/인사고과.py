def solution(scores):
    wanho=scores[0]
    # print(wanho)
    ordered_list=sorted(scores,key=lambda x: (-x[0],x[1]))
    prev_x=ordered_list[0][0]
    prev_y=ordered_list[0][1]
    # print(ordered_list)
    remain=[]
    for x,y in ordered_list:
        if x<prev_x and y<prev_y:
            continue
        prev_x=x
        prev_y=y
        remain.append([x,y])
        
    remain.sort(key=lambda x:(x[0]+x[1]),reverse=True)
    # print(remain)
    if wanho not in remain:
        return -1
    for idx,[x,y] in enumerate(remain):
        if wanho[0]+wanho[1]==x+y:
            return idx+1
    
    
    return idx+1