s="amfoss"

n=int(input())
l=[]
for i in range(n):
    count=0
    c=input()
    for i in range(6):
        if c[i]!=s[i]:
            count+=1
    l.append(count)
for i in l:
    print(i)
        