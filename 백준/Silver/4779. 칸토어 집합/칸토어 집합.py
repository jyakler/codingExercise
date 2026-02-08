import sys

input = sys.stdin.readline
dp = ["" for _ in range(13)]
start = "-"
dp[0] = "-"
for i in range(1, 13):
    dp[i] = dp[i-1]+(" "*(3**(i-1))) + dp[i-1]

# i = int(input())
# print(dp[i])

while True:
    n = input()
    if n == "":
        break
    else:
        print(dp[int(n)])
