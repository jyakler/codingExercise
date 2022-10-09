# 프로그래머스 문제 level 1

[신고결과받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

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
