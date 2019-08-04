T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split(' ')))
    B=list(map(int,input().split(' ')))
    S=[]
    for i in range(N):
        S.append(20*A[i]-10*B[i])
    maxValue = max(S)
    if maxValue<0:
        maxValue = 0
    print(maxValue)
