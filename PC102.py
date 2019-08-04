T=int(input())
for _ in range(T):
    N=int(input())
    a=input()
    sum=[]
    no="2357"
    str=""
    for i in range(N):
        if a[i] in no:
            sum.append(a[i])
        elif a[i]=='4':
            sum.append('2')
            sum.append('2')
            sum.append('3')
        elif a[i]=='6':
            sum.append('5')
            sum.append('3')
        elif a[i]=='8':
            sum.append('7')
            sum.append('2')
            sum.append('2')
            sum.append('2')
        elif a[i]=='9':
            sum.append('7')
            sum.append('3')
            sum.append('3')
            sum.append('2')
    sum.sort()
    sum.reverse()
    str=''.join(sum)
    print(str)
