s=input()
w="hello"
check=True
st="h"
c=0

for i in s:
    if i==st:
        c+=1
        st=w[c]
    if c==4:
        check=False
        break
if check==True:
    print("NO")
else:
    print("YES")