T=int(input())
for _ in range(T):
    S=input()
    if S.count('1')&1==0:
        str="LOSE"
    else:
        str="WIN"
    print(str)
