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
