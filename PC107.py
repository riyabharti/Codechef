T=int(input())
for _ in range(T):
    pos= [0]*26
    neg={}
    c=1
    count=0
    n=int(input())
    for i in range(n):
        a=input()
        x=ord(a[0])-97
        y=ord(a[3])-97
            
        if(a[1]=='!'):
            if a[0] in neg:
                neg[a[0]]+=a[3]
            else:
                neg[a[0]]=a[3]
        else:
            if(pos[x]==0 and pos[y]==0):
                pos[x]=c
                pos[y]=c
                c+=1
            elif(pos[x]==0 and pos[y]!=0):
                pos[x]=pos[y]
            elif(pos[x]!=0 and pos[y]==0):
                pos[y]=pos[x]
            else:
                f=pos[y]
                pos[y]=pos[x]
                while f in pos:
                    i=pos.index(f)
                    pos[i]=pos[x]
    while(max(pos)>0):
        ex=max(pos)
        dex=pos.index(ex)
        pos[dex]=-1
        while max(pos)==ex:
            print("PLO")
            n=pos.index(max(pos))
            if chr(dex+97) in neg:
                if chr(n+97) in neg[chr(dex+97)]:
                    count=1
                    break
                pos[n]=0
            else:
                break
        if count==1:
            break
    if count==1:
        print("No")
    else:
        print("Yes")
            
        
        
            
        
