t=int(input())
for i in range(t):
    n=int(input())
    small1=0
    small2=0
    a=[]
    b=[]
    l=list(map(int,input().split()))
    l.sort()
    for i in l:
        if i not in a:
            a.append(i)
        else:
            b.append(i)
    if a==[]:
        small1=0
    else:
        c=0
        while True:
            
            if c not in a:
                small1=c
                break
            c+=1
    if b==[]:
        small2=0
    else:
        c=0
        while True:
            
            if c not in b:
                small2=c
                break
            c+=1
    print(small1+small2)