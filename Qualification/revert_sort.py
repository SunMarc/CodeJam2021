def solution(n,L):
    ans=0
    for i in range(n-1):
        j = L.index(min(L[i:]))
        L=L[:i]+L[i:j+1][::-1]+L[j+1:]
        ans+=j-i+1
    return(ans)

for i in range(int(input())):
    n = int(input())
    L= list(map(int,input().split(" ")))
    ans = solution(n,L)
    print(f"Case #{i+1}: {ans}")
