import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

dp = []

def binary(num, array):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low+high)//2
        # print(low, mid, high, array[mid], num)
        if array[mid] == num:
            return mid
        if num > array[mid]:
            low = mid+1
        else:
            high = mid-1
    return low


for i in array:
    if len(dp) == 0:
        dp.append(i)
        continue
    index = binary(i, dp)
    # print(dp)
    # print(index)
    if (index > len(dp)-1):
        dp.append(i)
    else:
        dp[index] = i

print(len(dp))
