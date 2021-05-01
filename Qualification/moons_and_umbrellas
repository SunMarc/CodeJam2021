import math
def solution(X,Y,S):
    points={"CJ":X,"JC":Y,"CC":0,"JJ":0}
    rel={"C":0,"J":1}
    dp=[[math.inf,math.inf] for i in range(len(S))]
    dp[0]=[0,0]
    for i in range(1,len(S)):
        if S[i-1]=="?" and S[i]=="?":
            dp[i][0]=min(dp[i-1][0],dp[i-1][1]+points["JC"])
            dp[i][1]=min(dp[i-1][0]+points["CJ"],dp[i-1][1])
        elif S[i-1]=="?" and S[i]!="?":
            dp[i][rel[S[i]]]=min(dp[i-1][0]+points["C"+S[i]],dp[i-1][1]+points["J"+S[i]])
        elif S[i-1]!="?" and S[i]=="?":
            dp[i][0]=dp[i-1][rel[S[i-1]]]+points[S[i-1]+"C"]
            dp[i][1]=dp[i-1][rel[S[i-1]]]+points[S[i-1]+"J"]
        elif S[i-1]!="?" and S[i]!="?":
            dp[i][rel[S[i]]]=dp[i-1][rel[S[i-1]]]+points[S[i-1]+S[i]]
    return(min(dp[-1]))
    
for i in range(int(input())):
    X,Y,S= map(str,input().split(" "))
    X=int(X)
    Y=int(Y)
    ans = solution(X,Y,S)
    print(f"Case #{i+1}: {ans}")
