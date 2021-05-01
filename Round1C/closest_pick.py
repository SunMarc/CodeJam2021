def solution(N,K,P):
    P=[0]+P+[K+1]
    available = []
    for j in range(0,len(P)-1):
        available.append(P[j+1]-P[j]-1)
    best = available[0]+available[-1]
    for i in range(1,len(available)-1):
        best = max(best,((available[i]+1)//2)+available[0])
        best = max(best,((available[i]+1)//2)+available[-1])
        best = max(best,available[i])
    for i in range(1,len(available)-1):
        for j in range(i+1,len(available)-1):
            best = max(best,(available[i]+1)//2+(available[j]+1)//2)
    return(best/K)
        
for i in range(int(input())):
    N,K= map(int,input().split(" "))
    P = sorted(list(set(map(int,input().split(" ")))))
    ans = solution(N,K,P)
    print(f"Case #{i+1}: {ans}" )
