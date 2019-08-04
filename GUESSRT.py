z=1000000007
def poww(N,M,K=z):
    if M==0:
        return 1
    hf=poww(N,int(M/2))
    if M%2==0:
        return (hf*hf)%K
    else:
        return (hf*hf*N)%K

T=int(input())
for _ in range(T):
    N,K,M=map(int,input().split())
    p=poww(N-1,(M+1)//2)  
    q=poww(N,int((M+1)/2))
    if M%2==0:
        p=p*(N+K-1)%z
        q=(q*(N+K))%z
    p=q-p
    
    print((p*poww(q,z-2))%z)
