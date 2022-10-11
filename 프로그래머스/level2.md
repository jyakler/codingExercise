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
