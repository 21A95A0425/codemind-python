a=int(input())
b=list(map(int,input().split()))
c=max(b)
d=c
e=0
while True:
    for i in b:
        if c%i==0:
            e+=1
    if e==a:
        print(c)
        break
    else:
        e=0
        c+=d
        