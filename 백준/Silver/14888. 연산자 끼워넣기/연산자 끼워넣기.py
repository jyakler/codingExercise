import sys
from itertools import permutations
import math
input = sys.stdin.readline


def solution(l: int, num: list, operation: list):
    min_result = 2**63-1
    max_result = -2**63-1
    per = set(permutations(operation, l-1))
    for i in per:
        result = create_operation2(l, num, i)
        min_result = min(min_result, result)
        max_result = max(max_result, result)
    print(max_result)
    print(min_result)


def create_operation2(l, num, operation):
    result = num[0]
    for i in range(1, l):
        if (operation[i-1] == "+"):
            result += num[i]
        if (operation[i-1] == "-"):
            result -= num[i]
        if (operation[i-1] == "*"):
            result *= num[i]
        if (operation[i-1] == "//"):
            if (result < 0):
                result = -((-result)//num[i])
            else:
                result //= num[i]

    return result


N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
operation = []
for i in range(op[0]):
    operation.append("+")
for i in range(op[1]):
    operation.append("-")
for i in range(op[2]):
    operation.append("*")
for i in range(op[3]):
    operation.append("//")

solution(N, num, operation)
