T=int(input())
for _ in range(T):
    N=int(input())
    C=list(map(int,input().split()))
    C.insert(0,0)
    Rp=[0]*(N+2)
    H=list(map(int,input().split()))
    for i in range(1,N+1):
        if i-C[i]<1:
            lb=1
        else:
            lb=i-C[i]
        if i+C[i]>N:
            ub=N+1
        else:
            ub=i+1+C[i]
            
        #creating prefix sum array
        Rp[lb]+=1
        Rp[ub]-=1

    for i in range(1,N+2):
        Rp[i]+=Rp[i-1]

    Rp.remove(0)
    Rp.remove(0)
    H.sort()
    Rp.sort()
    
    if H==Rp:
        print("YES")
    else:
        print("NO")
     
    
