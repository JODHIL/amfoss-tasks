t=int(input())
s=0
x=[]
y=[]
z=[]
for i in range(t):
    x1,y1,z1=map(int,input().split())
    x.append(x1)
    y.append(y1)
    z.append(z1)
if sum(x)==sum(y)==sum(z)==0:
    print("YES")
else:
    print("NO")