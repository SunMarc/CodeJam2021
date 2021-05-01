def solution(N,C):
    def bin_search(C,n):
        i=1
        j=N-n+1
        while i<j:
            mid = (i+j)//2
            value = mid+(N-n-1)
            if C<value:
                j=mid-1
            elif C>value:
                i=mid+1
            else:
                return(mid)
        return(i if i+(N-n-1)<=C else i-1)

    def backtrack(C,ans,n):
        if C==0 and n==N:
            ans[-1]=[ans[-1],N]
            return(ans)
        else:
            r = bin_search(C,n)
            #print(r)
            #print(ans[n-1:n+r-1])
            inverse = ans[n-1:n+r-1]
            inverse[r-1]=[inverse[r-1],n]
            inverse = inverse[::-1]
            #print(ans[:n-1]+inverse+ans[n+r-1:])
            #print(N,C)
            return(backtrack(C-r,ans[:n-1]+inverse+ans[n+r-1:],n+1))
    if C<N-1 or C>(N+1)*N//2-1:
        return("IMPOSSIBLE")
    else:
        return(backtrack(C,[i for i in range(0,N)],1))

for i in range(int(input())):
    N, C = list(map(int,input().split(" ")))
    _ans = solution(N, C)
    if _ans!="IMPOSSIBLE":
        ans = [0 for i in range(N)]
        for j in range(len(ans)):
            ans[_ans[j][0]]=str(_ans[j][1])
        ans=" ".join(ans)
        print(f"Case #{i+1}: {ans}")
    else:
        print(f"Case #{i+1}: {_ans}")



