![캡처](https://user-images.githubusercontent.com/49812691/167856413-ba97c83f-4e09-4529-9d40-fcdd4a7f181c.PNG)

[문제11066](https://www.acmicpc.net/problem/11066)

처음에는 11066을 해결하려 하였는데 막상 코드를 구현하고나니 모든장을 연속이 되도록 합치는 작업이 아닌 순서를 섞어 작업을 하였음.

이에 대한 문제가 13975로 존재하기에 13975 문제로 제출함

는 시간초과가 걸려버림

배열을 받아 insertion sort를 돌리고 하나 계산할때마다 삽입 정렬을 돌리다보니 
최악의 경우 O(n^2)+O(n!)가 되버려 오버가 된것으로 추정.

찾아보다보니 import heapq 를 사용해서 heap사용시 시간이 단축될것 같음

수정하고 제출하니 정답! 다만 시간이 빠듯하게 된듯