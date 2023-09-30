
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a,b=0,1
    s=0
    while True:
        a,b=b,a+b
        if b<=n:
            if b%2==0:
                s+=b
        else:
            break
    print(s)
                
        