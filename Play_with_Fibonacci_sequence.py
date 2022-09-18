z=int(input())
c=2
a=0
b=1
s=0
if z==1:
    print(0)
elif z==2:
    print(0,1)
else:
    print(0,end=" ")
    while c<=z:
        a=b
        b=s
        s=a+b
        print(s,end=" ")
        c+=1