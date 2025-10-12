def solution(info, n, m):
    answer = 0
    # knapsack
    info_sort=sorted(info,key=lambda x:x[0]/x[1],reverse=True)
    print(info_sort)
    A=0
    B=0
    for i in info_sort:
        if m>B+i[1]:
            B+=i[1]
        elif n<=A+i[0]:
            return -1
        else:
            A+=i[0]
    return A