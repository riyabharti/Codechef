#correct
T=int(input())
for _ in range(T):
    N=int(input())
    S=list(map(int,input().split()))
    S.sort()
    m=max(S)
    for i in range(N-1):
        t=S[i+1]-S[i]
        if(abs(t)<m):
            m=abs(t)
    print(m)
