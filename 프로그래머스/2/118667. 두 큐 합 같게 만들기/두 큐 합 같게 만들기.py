from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    total=sum(queue1)+sum(queue2)
    tl=len(queue1)+len(queue2)
    target=total/2
    current=sum(queue1)
    while answer<tl*2:
        if current==target:
            break
        if current>target:
            answer+=1
            p=queue1.popleft()
            current-=p
            queue2.append(p)
        else:
            answer+=1
            p=queue2.popleft()
            current+=p
            queue1.append(p)
    if answer>=tl*2:
        return -1
            
    
    return answer