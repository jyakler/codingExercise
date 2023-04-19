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
(2023-04-12)
```python
def solution(clothes):
    all_clothes=dict()
    for _, types in clothes:
        all_clothes[types]=all_clothes.get(types,1)+1
    diff=1
    for _, value in all_clothes.items():
        diff*=value
    return diff-1
```
코테 준비겸 다시 예전에 풀었던 문제도 다지우고 풀어보고있는데 확실히 예전에 짠것보다 더 쉽게 짜는 것 같음

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

(2023-04-07)

[기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3)

```python
def solution(progresses, speeds):
    answer = []
    current_list=progresses
    while len(current_list):
        current_list=[x+y for x,y in zip(current_list,speeds)]
        if current_list[0]>=100:
            flag=check(current_list)

            if flag==-1:
                answer.append(len(current_list))
                return answer
            else:
                answer.append(flag)
                current_list=current_list[flag:]
                speeds=speeds[flag:]


def check(current_list):
    for i,v in enumerate(current_list):
        if v<100:
            return i
    return -1
```
대기열 걸린것같은 큐 만드는 문제.

뭔가 머리속으로 speed와 progress를 더하면서 경과보는게 직관적이라 그렇게 짰는데 제한이 없어서 바로 통과

(2023-04-17)

[큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)
```python
def solution(number, k):
    answer=''
    stack=[]
    left=len(number)
    out=0
    for i in number:
        if out==k:
            stack.append(i)
            continue
        if not stack:
            stack.append(i)
        else:
            while stack:
                if stack[-1]<i:
                    stack.pop()
                    out+=1
                else:
                    break
                if out==k:
                    break
            stack.append(i)
    return ''.join(stack[:left-k])
```
처음에는 stack으로 구현하지 않고 list로 구현하면서  len()-k개의 자리를 보면서 찾은 max의 index를 가지고 그 다음 루프는 index+1부터 len()-k+1 이런식으로 보면서 하였는데, 정답은 맞지만 효율성에서 빠꾸를 먹음.

Greedy알고리즘인 만큼 단순하게 2개씩 비교하면서 스택으로 쌓았더니 쉽게 해결... 쉬운문제를 1시간좀 넘게 고민함

(2023-04-19)

[H-index](https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3)
```python
def solution(citations):
    n=len(citations)
    # sorted_array=sorted(citations)
    max_c=0
    for h in range(1,n+1):
        if len([i for i in citations if i>=h])>=h:
            max_c=h
        else: break
    return max_c
```
처음에는 h index가 도대체 뭔말인지 이해못해서 학자가낸 논문의 인용횟수 h 를 가지고 하는것인줄알았는데

자료 찾아보니까 그냥 h가 꼭 논문의 인용회수에 등장하는 숫자가 아니여도 된다는 것을 안 후는 너무 쉬웠음.

효율성문제가 있었다면 O(n^2)라서 어떻게 될지는 모르겠지만 아무튼 테스트는 통과

```python
def solution(citations):
    n=len(citations)
    sorted_array=sorted(citations)
    for i in range(n):
        if sorted_array[i]>=n-i:
            return n-i
    return 0
```
정렬 함수가 O(nlogn)이라 이거써서 좀 줄여보려했음. 우선 n개(전체)가 답이될거면 제일 처음께(제일작은게) n이상이여야 하고 두번재꺼는 n-1이상 ... 이런식으로 진행되서 구현함

```python
def solution(citations):
    return max(map(min,enumerate(sorted(citations,reverse=True),start=1)))
```
역시 한줄로 구현했었던 사람이 있어서 가져옴. 코드 자체는 위에 짠것을 reverse order로 보는 것