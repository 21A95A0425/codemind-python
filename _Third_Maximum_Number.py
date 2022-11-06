a=int(input())
b=list(map(int,input().split()))
b=set(b)
b=list(b)
if len(b)<3:
    print(max(b))
else:
    
    c=max(b)
    z=b.index(c)
    b.pop(z)
    c=max(b)
    z=b.index(c)
    b.pop(z)
    print(max(b))

