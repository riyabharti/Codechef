T=int(input())
for _ in range(T):
    s1=input()
    s2=input()
    i=0
    alphabets="abcdefghijklmnopqrstuvwxyz"
    s1=s1.lower()
    s2=s2.lower()
    for key in alphabets:
        if(s1.count(key)<s2.count(key)):
            i=1
            break
    if i==1:
        print("no")
    else:
        print("yes")
        
