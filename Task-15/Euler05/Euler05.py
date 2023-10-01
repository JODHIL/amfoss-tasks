

import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s=1
    for i in range(2,n+1):
        l=s*i//math.gcd(s,i)
        s=l
    print(s)
    
        