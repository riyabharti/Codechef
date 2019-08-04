z=1000000007
def poww(N,M,K=z):
    if M==0:
        return 1
    if M==1:
        return N
    hf=poww(N,int(M/2))
    if M%2==0:
        return ((hf%K)*(hf%K))%K
    else:
        return ((hf%K)*(hf%K)*(N%K))%K
    
T=int(input())
for _ in range(T):
    N,P=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    sum=0
    while i<N:
        for j in range(i+1,i+1+a[i]):
            if j>=N:
                break
            sum=((sum % z)+poww(a[j],a[i],z))%z
        i=i+a[i]+1

    sum=((sum%z)*(P%z))%z
    print(sum)
