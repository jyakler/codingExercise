[N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3)(DP)
-----
```python 
def calculate(a,b):
    temp_set=set()
    for i in a:
        for j in b:
            temp_set.add(i+j)
            temp_set.add(i-j)
            if j!=0:
                temp_set.add(i//j)
            temp_set.add(i*j)
    return temp_set
    
def solution(N, number):
    d=dict()
    for i in range(0,9):
        d[i] = d.get(i,set())
    d[0].add(0)
    for i in range(1,9):
        if int(str(N)*i)<=32000:
            d[i].add(int(str(N)*i))

    for i in range(2,9):
        for j in range(1,i):
            k=i-j
            d[i].update(calculate(d[j],d[k]))
    for i in range(9):
        if number in d[i]:
            return i
    return -1
```
처음 고민했을때는 그냥 사칙연산만 생각해서 N으로 사칙연산을 통해 나오는 값이 한정되어있다 생각 했다.

n/n=1,  nn/n=11,  nnn/n=111 같이 나올 수있는 값이 일정하다 생각했는데

$12=(55+5)/2$ 이 예시를 보고 다시 처음부터 생각해야 했다.

오래 고민하다가 도저히 몰라서 블로그에서 해당문제의 접근방식을 읽었다. 1번 연산해서 얻을 수 있는 숫자-> 2번 연산해서 얻을 수 있는 숫자 .... 이런식으로 접근한다는 것을 보고

바로 직접 코드를 짜보았다. 접근 방식만 알면 생각보다 문제가 쉽게 풀리는 느낌을 받았음

