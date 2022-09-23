z=int(input())
y=list(map(int,input().split()))
a=sum(y)
if a%2==0 and z%2==0:
    c=0
    b=0
    for i in y:
        if i%2:
            c+=1
        else:
            b+=1
    if c%2==0 and b%2==0:
        print(1)
    else:
        print(0)
else:
    print(0)