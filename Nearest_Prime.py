for _ in range(int(input())):
    a=int(input())
    n=a
    while True:
        b=[]
        for i in range(1,n+1):
            if n%i==0:
                b.append(i)
        if len(b)==2:
            break
        n+=1
    z=a-1
    while True:
        x=[]
        for i in range(1,z+1):
            if z%i==0:
                x.append(i)
        if len(x)==2:
            break
        z-=1
    y=a-z
    x=n-a
    if y<=x:
        print(z)
    else:
        print(n)

    