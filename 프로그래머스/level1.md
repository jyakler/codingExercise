# 프로그래머스 문제 level 1

(2022/10/9)

[신고결과받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)
---------
```python
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reports={x:0 for x in id_list}
    #신고
    for i in set(report):
        reports[i.split()[1]]+=1
    #신고확인
    for i in set(report):
        if reports[i.split()[1]]>=k:
            answer[id_list.index(i.split()[0])]+=1
    return answer
```

처음에는  dict을 사용해야한다고 생각은 했지만 코드상 구현방법이 생각이 안나 대채 방안으로 pandas dataframe과 re 의 match를 사용해서 신고 결과를 찾는 방식으로 하려했는데

아무리 생각해봐도 너무 복잡하고 삥돌아간 방법이라 dict를 사용하는 다른 분꺼 코드를 보고  어떻게 구현해야겠다는 감잡은후 문제 풀이 진행함


[크레인 인형뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061)
----------
```python
def solution(board, moves):
    answer = 0
    game=[]
    #보드로 새로운 stack만듬
    l=len(board)
    n_board=[[]*1 for _ in range(l)]
    for i in range(l):
        for j in range(l-1,-1,-1):
            if board[j][i]!=0:
                n_board[i].append(board[j][i])
    print(n_board)
    #moves
    for i in moves:
        try:
            p=n_board[i-1].pop()
            if game:
                if game[-1]==p:
                    game.pop()
                    answer+=2
                    continue
            game.append(p)
        except:
            pass
    return answer
```
우선 인형을 뽑는 것처럼 list에서 pop하고 싶었기에 처음 주어진 board 구조로는 어려움이 있어서 새로운 list 배열을 생성해서 사용함

근데 다른사람 풀이를 보니 굳이 그렇게 구현하지 않고도 뽑은 범위를 0 으로 만들면 되었음 ㅜㅜ


[완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)
------------
```python
def solution(participant, completion):
    answer = ''
    for i in completion:
        participant.remove(i)
    return participant[0]
```
그냥 리스트에서 제거하면서 하면 될 것같았는데 정답은 맞았지만 효율성 테스트에서 시간초과로 오답이 나옴

입력값이 10만이기때문에 dict사용하면 될 것같음

```python
def solution(participant, completion):
    dict={}
    for key in participant:
        dict[key]=dict.get(key,0)+1
    for k in completion:
        dict[k]-=1
    return [i for i in dict if dict[i]>0][0]
```

사실 위에서도 적었지만 dict구현방법은 예전 학부시절 몇번 써보긴했는데 기억이 안나서 해당 코드 다시열어서 내가 짰던 것 참고함...

list index, append ,pop는 O(1)로 알고있는데 위의 코드가 왜 time out 됬는지 궁금했는데 remove는 O(N)였던것.. for루프안에서 썼으니 $N^2$ 였던 것

(2022/10/10)

[키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256)
----------
