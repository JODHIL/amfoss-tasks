n=int(input())
x=list(map(int,input().split()))
s=x[0]
index=0
check=False
y=list(x)
y.sort()


if y[0]==y[1]:
    check=True
if check==True:
    print("Still Aetheria")
else:
    print(x.index(y[0])+1)