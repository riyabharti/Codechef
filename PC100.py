T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    if K in a:
        print("Yes")
    else:
        print("No")
