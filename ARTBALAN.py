T=int(input())
for _ in range(T):
    S=input()
    n=len(S)
    dict={}
    alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #O(26)
    for key in alphabets:     
        dict[key]=S.count(key)

    factors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            factors.append(i)
            factors.append(int(n/i))

    F=sorted(factors)
    
    final=[]
    for i in F:
        s=[]
        for key in alphabets:
            if dict[key]!=0:
                x=int(n/i)-dict[key]
                s.append(x)
        
        pos=0
        neg=0
        for j in range(i):
            if s:
                if min(s)>0:
                    pos+=min(s)
                neg+=min(s)
                s.remove(min(s))
                #print("if",pos,neg)
            else:
                
                for key in alphabets:
                    if dict[key]==0:
                        #print("else",pos,neg)
                        pos+=n//i
                        #print(pos,neg)
                        neg+=n//i
                        #print(pos,neg)
                    if neg==0:
                        break
                if neg!=0:
                    pos=n
                        
                break
        if pos!=n:
            final.append(pos)       
    
    print(min(final))        
