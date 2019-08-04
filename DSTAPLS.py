T=int(input())
for _ in range(T):
    str="YES"
    N,K=map(int,input().split(' '))
    if(K==1):
        str="NO"
    elif N%(K*K)==0:
        str="NO"
    print(str) 
