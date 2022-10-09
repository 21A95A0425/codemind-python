z=input()
z=z.casefold()
a=z.split()
d=''
if len(a)==1:
    print(-1)
else:
    b=a[0]
    for i in b:
        f=False
        for k in a:
            if i in k:
                f=True
            else:
                f=False
                break
        if f==True:
            d=d+i
            for j in a:
                for p in range(len(j)):
                    if j[p]==i:
                        j=j[:p]+j[p+1:]
                        break
    if len(d)==0:
        print(-1)
    else:
        print(d)