T=int(input())
#LCM
for _ in range(T):
    n,a,b,k=map(int,input().split())
    s=int(n/a)+int(n/b)
    y=a*b
    while(b):
       a, b = b, a % b
    
    x=int(y/a)
    x=int(n/x)
    s=s-2*x
    if(s>=k):
        print("Win")
    else:
        print("Lose")
