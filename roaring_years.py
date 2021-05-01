def solution(Y):
    def roaring(i):
        number = str(i)
        for t in range(1,len(number)//2+1):
            init = int(number[:t])
            string = number[:t]
            while len(string)<len(number):
                string+=str(init+1)
                init+=1
            if int(string)==i:
                return(True)
        return(False)
    
    i = Y+1
    while True:
        if roaring(i):
            return(i)
        else:
            i+=1
                
            
        
for i in range(int(input())):
    Y = int(input())
    ans = solution(Y)
    print(f"Case #{i+1}: {ans}" )
