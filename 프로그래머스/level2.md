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
