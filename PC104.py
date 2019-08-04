t=int(input())
for _ in range(t):
    n=int(input())
    B=list(map(int,input().split()))
    A=list(set(B))
    print(sum(A))
