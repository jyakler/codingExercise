from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    total=sum(queue1)+sum(queue2)
    tl=len(queue1)+len(queue2)
    target=total/2
    while 1:
        if answer>tl:
            answer=-1
            break
        if sum(queue1)==target:
            break
        elif sum(queue1)>target:
            answer+=1
            queue2.append(queue1.popleft())
        else:
            answer+=1
            queue1.append(queue2.popleft())
            
            
    
    return answer