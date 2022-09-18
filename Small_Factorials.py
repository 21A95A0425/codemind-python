a=int(input())
s=1
for i in range(1,a+1):
    m=int(input())
    k=m
    while k!=0:
        s=s*k
        k-=1
    print(s)
    s=1