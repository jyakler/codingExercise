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

[정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=python3)
-------
```python
def solution(triangle):
    answer = 0
    l=len(triangle)
    dp=[[0]*l for _ in range(l)]
    dp[0][0]=triangle[0][0]
    for i in range(0,l-1):
        for j in range(i+1):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j]+triangle[i+1][j])
            dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+triangle[i+1][j+1])
    return max(dp[l-1])
```
DP 문제의 정석 예시로 처음 배울 때 해보았던 코드라 금방 짤 수 있었음.


[섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3#)(Greedy)(MST문제)
--------
```python
def solution(n, costs):
    answer = 0
    v=[0 for _ in range(n)]

    d={}
    for s,e,c in costs:
        d[c]=d.get(c,list())+[(s,e)]
    # print(d)
    while(sum(v)!=n):
        print(d)
        print(v)
        for a,b in d[min(d)]:
            if v[a]==0 or v[b]==0:
                v[a]=1
                v[b]=1
                answer+=min(d)
        del d[min(d)]
    return answer
"""
첫풀이= 최소 cost만 찾아서 잇는거 하려했는데 동떨어진 2개의 꼭지점을 계산해버리면 오류발생
"""
```
처음에는 min cost선분부터 고르는 식으로 했는데  min cost가 동떨어진곳에서 발생하면 오류가 생겼음

예전에 배웠던 알고리즘 생각해서 했던건데 나중에 찾아보니 Kruskal 알고리즘을 사용하려했었던 거였음

```python
def solution(n, costs):
    answer = 0
    m=set()
    d={}
    for s,e,c in costs:
        d[c]=d.get(c,list())+[(s,e)]
    while(len(m)!=n):
        for a,b in d[min(d)]:
            if len(m)==0:
                print(a,b)
                print(min(d))
                m.update([a,b])
                answer+=min(d)
                continue
            if ((a in m) ^ (b in m))==1:
                m.update([a,b])
                print(a,b)
                print(min(d))
                answer+=min(d)
        del d[min(d)]
    return answer

"""
집단 안에있는 vertex에서 이어져있는 놈 중 min을 고르는데 루프는 전체의 min부터 보다보니까 하나 건너서 돌아가야할때 못돌아감
"""
```
그래서 min부터 돌되 메인 집합에 포함되어있는 애가 있어야지 계산하도록했는데 그게 최소가 아니라 나중에 다시 최소값을 찾아야할때 못찼았음.

여기서 조금 수정하면 풀릴 것같았는데 그냥 처음부터 다시 풀어봄

```python
def solution(n, costs):
    v=[[]*1 for _ in range(n)]
    m=1e9
    a=-1
    b=-1
    for s,e,c in costs:
        if m>c:
            m=c
            a=s
            b=e
        v[s].append((c,e))
        v[e].append((c,s))
    r=v[a]+v[b]
    l=[a,b]
    answer=m
    r.sort(reverse=True)
    while(len(l)!=n):  
        c,s=r.pop()
        if s in l:
            continue
        else:
            l.append(s)
            r+=v[s]
            r.sort(reverse=True)
            answer+=c

    return answer
```
이게 다익스트라였나 했는데 프림알고리즘이였음 

확실히 학부때 들은건 있어서 써보려하는데 너무 대충 알고있는 것 같음..

매번 sort하는게 마음에 안들고 뭔가 heapq를 써보고싶어서 다시만듬
```python
import heapq
def solution(n, costs):
    v=[[]*1 for _ in range(n)]
    m=1e9
    a=-1
    b=-1
    for s,e,c in costs:
        if m>c:
            m=c
            a=s
            b=e
        v[s].append((c,e))
        v[e].append((c,s))
    r=v[a]+v[b]
    l=[a,b]
    answer=m
    r.sort()
    while(len(l)!=n):  
        c,s=heapq.heappop(r)
        if s in l:
            continue
        else:
            l.append(s)
            for i in v[s]:
                heapq.heappush(r,i)
            answer+=c
    return answer
```
sort를 덜하니까 좀더 빠를 줄 알았는데 heappush를 계속 해서 그런지 느림... 테케기준으로는 이게 시간이 더 오래걸림


[가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3)
------
```python
def solution(n, edge):
    answer = 0
    v=[[]*1 for _ in range(n)]
    r=[1e9 for _ in range(n)]
    r[0]=0
    for s,e in edge:
        v[s-1].append(e-1)
        v[e-1].append(s-1)
    q=[0]#queue
    d=[]#done
    while q:
        j=q.pop()
        d.append(j)
        for i in v[j]:
            if i in d:
                continue
            else:
                r[i]=min(r[i],r[j]+1)
                q.append(i)
    m=max(r)
    return len([i for i,e in enumerate(r) if e==m])
```
처음에 짰던 코드인데 테케 5,7,9 가 틀려서 왜 틀렸나했는데 list에 중간에 뭐가 추가되는데 pop이 queue가아니라 stack방식으로 작용하기에 연산이 잘못된거였음

그래서 deque사용해서 아래와 같이 함
```python
from collections import deque
def solution(n, edge):
    answer = 0
    v=[[]*1 for _ in range(n)]
    r=[1e9 for _ in range(n)]
    visited=[0 for _ in range(n)]
    r[0]=0
    for s,e in edge:
        v[s-1].append(e-1)
        v[e-1].append(s-1)
    q=deque()
    q.append(0)
    while q:
        i=q.popleft()
        if visited[i]!=0:
            continue
        visited[i]=1
        for e in v[i]:
            r[e]=min(r[e],r[i]+1)
            q+=[e]
    m=max(r)
    return len([i for i,e in enumerate(r) if e==m])
```

[네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3)(DFS,BFS)
----------
```python
def solution(n, computers):
    parent=[i for i in range(n)]
    for i,x in enumerate(computers):
        for k in range(n):
            if x[k]!=1:
                continue
            if k==i:
                continue
            unionparent(parent,x[k],i)
    return len(set(parent))

def getparent(parent,i):
    if parent[i]==i:
        return parent[i]
    return getparent(parent,parent[i])

def unionparent(parent,a,b):
    a=getparent(parent,a)
    b=getparent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
```
전에 섬연결 문제에서 다른사람이 union and find방식으로 푸는 것을 보고 이문제를 보았을때 그걸 활용하면 되겠다고 생각해서 시도해봄

근데 unionparent(parent,`x[k]` k대신 써서 일단 여기서 에러였고 두번째로는 아래 그림같은 케이스일때 오류가 떴음

의아했던거는 맞으면 안될 것같은 코드가 테케 2,4,7인가? 를 제외하고 맞았다는 것

![image](https://user-images.githubusercontent.com/49812691/195991930-86b1dace-2d5c-44ac-b8e0-70c53e106d8a.png)

그것을 수정한게 다음 코드
```python
def solution(n, computers):
    parent=[i for i in range(n)]
    for i,x in enumerate(computers):
        for k in range(n):
            if x[k]!=1:
                continue
            # if k==i:
            #     continue
            unionparent(parent,k,i)
    for i in range(n):
        getparent(parent, i)
    return len(set(parent))

def getparent(parent,i):
    if parent[i]!=i:
        parent[i]=getparent(parent,parent[i])
    return parent[i]

def unionparent(parent,a,b):
    a=getparent(parent,a)
    b=getparent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
```

우선 unionparent부분 수정하고 맨 마지막에 parent를 돌면서 한번씩 getparent를 써서 누락된것을 바꿔주는 작업을 거침
