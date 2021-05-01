def solution(X,Y):
    X=int(X,2)
    Y=int(Y,2)
    liste=[X]
    def bit_not(n, numbits):
        return (1 << numbits) - 1 - n
    if X == Y:
        return(0)
    for i in range(1,15):
        liste_bis=[]
        for l in liste:
            a = bit_not(l,len(str(bin(l)))-2)
            b = l<<1
            if a == Y or b == Y:
                return(i)
            liste_bis.append(bit_not(l,len(str(bin(l)))-2))
            liste_bis.append(l<<1)
        liste=liste_bis
    return("IMPOSSIBLE")
        
for i in range(int(input())):
    X,Y=input().split(" ")
    ans = solution(X,Y)
    print(f"Case #{i+1}: {ans}")
