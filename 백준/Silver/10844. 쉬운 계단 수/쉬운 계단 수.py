import sys
input = sys.stdin.readline

"""
1 2 3 4 5 6 7 8 9

12 10
21 23
32 34
43 45
54 56
65 67
76 78
87 89
98


"""
N = int(input())
dp = [0 for _ in range(101)]
d = dict()
d[0] = 0
for i in range(1, 10):
    d[i] = 1


def cal(d):
    temp = [i for i in d.values()]
    # d초기화
    for i in range(10):
        d[i] = 0
    for idx, num in enumerate(temp):
        if idx != 0:
            d[idx-1] += num
        if idx != 9:
            d[idx+1] += num


for i in range(N-1):
    cal(d)
# print(d)
print(sum(d.values()) % 1_000_000_000)
