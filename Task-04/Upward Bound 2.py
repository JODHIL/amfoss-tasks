import math
t=int(input())
for test in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=list(l)
    c=0
    if n==1:
        print(0)
    else:
        check=True
        for j in range(n-1,0,-1):
            while l[j]<=l[j-1]:
                l[j-1]=math.floor(l[j-1]/2)
                c+=1
            if ((l[j]==1 and l[0]!=0) or l[j]==0):
                check=False
                break
        if check==False:
            print(-1)
        else:
            print(c)
    