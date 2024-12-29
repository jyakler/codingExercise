def solution(sequence):
    plus=[]
    for idx,v in enumerate(sequence):
        if idx%2==0:
            plus.append(v)
        else:
            plus.append(-v)
    minus=[-i for i in plus]
    # print(plus)
    
    dp=[i for i in plus]
    for i in range(1,len(plus)):
        if dp[i]<dp[i-1]+dp[i]:
            dp[i]+=dp[i-1]
            
    minus_dp=[i for i in minus]
    for i in range(1,len(minus)):
        if minus_dp[i]<minus_dp[i-1]+minus_dp[i]:
            minus_dp[i]+=minus_dp[i-1]
            
            
    # print(dp)
    # print(minus_dp)
    # [2,-3,-6,-1,3,1,2,-4]
    # [-2,3,6,1,-3,-1,-2,4]
    return max(max(dp),max(minus_dp))
