[전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3) (HASH)
----
```python
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][0:len(phone_book[i])]:
            return False
    return True
```
for 문을 돌려서 $n^2$ 번 돌리기에는 타임아웃될것같아서 패스

해시 문제라해서 겁먹고 또 dict사용해야하나 하고있었는데 의외로 간단하게 sort써서 그냥 앞의 len만큼 비교하면 끝이였다


[위장](https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3)
---------
```python
from itertools import combinations
import math
def solution(clothes):
    dic={}
    for clo,key in clothes:
        dic.setdefault(key,[]).append(clo)
    
    l=[len(i) for i in dic.values()]
    result=sum(l)
    for i in range(2,len(l)+1):
        b=list(combinations(l,i))
        for j in b:
            result+=math.prod(j)
    return result
```
처음에는 dict를 사용해야지~ 라 생각하면서 dict짰는데 기존 하던데로 dic.get(key,[])... 하니까 None으로 받아와져서 에러발생..

defaultdict 또는 setdefault사용해야함

근데 이게 왠걸 시간초과 ㅜㅜ

생각해보니 여러개 동전던져서 모두 뒷면이 나오는 경우만 제외한 것을 계산하는 것과 유사하다는 생각이 듬 그래서 dict만든 후 갯수 파악한뒤 +1 한것을 곱한다음 -1 해주었음

```python
import math
def solution(clothes):
    dic={}
    for clo,key in clothes:
        dic.setdefault(key,[]).append(clo)
    
    l=[len(i) for i in dic.values()]
    l=list(map(lambda x: x+1,l))
    return math.prod(l)-1
```


[가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3#)
----------
```python
def solution(numbers):
    answer = ''
    sn=list(map(str,numbers))
    sn.sort(key=lambda x:x*3,reverse=True)
    return str(int(''.join(sn)))
```
처음에는 sort할때 key값없이 그냥했다가 3<30이 되어서 330이 아니라 303이 만들어 졌기에 오류가 뜸

숫자가 0~1000사이의 숫자였기에 \*3를 해주어서 비교하니 답이 나왔는데 테케 11에서 틀림

찾아보니 0,0,0 이 들어올때 "000" 이 되도록 했어서 return할때 int로 잠깐 바꾸는 과정을 거침


[소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3)(완전탐색)
---------
```python
from itertools import permutations
def solution(numbers):
    answer = 0
    all_comb=list()
    l=[numbers[i] for i in range(len(numbers))]
    for i in range(1,len(l)+1):
        all_comb+=list(permutations(numbers,i))
    an=list(map(lambda x: int(''.join(x)),all_comb))
    for i in set(an):
        if i<2:
            continue
        for n in range(2,i):
            if i%n==0:
                answer-=1
                break
        answer+=1
    return answer
```
소수를 찾는 쉬운 방법이 생각이안나 그냥 2부터 다 나눠보는것으로 진행

[카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3)
---------
```python
def solution(brown, yellow):
    answer = []
    j=0
    for i in range(1,yellow+1):
        if yellow%i==0:
            j=yellow//i
            if (max(i,j)+2)*2+min(i,j)*2==brown:
                return [max(i,j)+2,min(i,j)+2]
    return answer
```
문제는 의외로 간단했음

갑자기 다른방식으로도 풀어보고 싶어서
```python
def solution(brown, yellow):
    answer = []
    j=(brown-4)//2
    for i in range(1,yellow+1):
        if yellow%i==0 and i+yellow//i==j:
            return [max(i,yellow//i)+2,min(i,yellow//i)+2]
    return answer
```
이렇게도 풀어보았음 같은건가....?


[전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971?language=python3)
------
```python
def solution(n, wires):
    answer = -1
    nodes=[[]*1 for _ in range(n)]
    r=[]

    for s,e in wires:
        nodes[s-1].append(e-1)
        nodes[e-1].append(s-1)
    for i in nodes:
        i.sort()
    for s,e in wires:
        c1=nodes[s-1].copy()
        c1.remove(e-1)
        c1.append(s-1)
        for i in c1:
            if i==s-1:
                continue
            for j in nodes[i]:
                if j not in c1 and j!=s-1:
                    c1.append(j)
        r.append(abs(n-2*len(c1)))
    return min(r)
```
최근에 풀었던 문제중 고민 많이 했던 것 같은 문제

처음 풀었을때는 테케 1에서 오류가나서 처음부터 갈아엎고 만듬

우선 각 노드에 연결된 노드를 nodes에 넣고 brute force방식처럼 하나하나 확인함

머릿속으로는 bfs, dfs로 풀면된다! 하는데 학부때 했던 구현방법이 기억안나서 이렇게 함

