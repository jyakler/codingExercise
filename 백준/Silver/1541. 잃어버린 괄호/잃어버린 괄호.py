import sys
input = sys.stdin.readline

result = 0

expression = input().strip()
i = 0
n = ""
isMinus = False

while i < len(expression):
    if expression[i] != "+" and expression[i] != "-":
        n += expression[i]
        i += 1
        continue
    current_num = int(n)
    n = ""

    if isMinus:
        result -= current_num
    else:
        result += current_num

    if (expression[i] == "-"):
        isMinus = True
    i += 1


current_num = int(n)

if isMinus:
    result -= current_num
else:
    result += current_num

print(result)
