T=int(input())
for _ in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    a.reverse()
    i=a.index(max(a))
    a.remove(max(a))
    j=a.index(max(a))
    if i<=j:
        print(N-j-1)
    else:
        print(N-j)
