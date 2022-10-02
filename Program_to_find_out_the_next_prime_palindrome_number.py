z=int(input())
c=0
while True:
    z+=1
    s=str(z)
    a=s[::-1]
    if z==int(a):
        for i in range(1,z+1):
            if z%i==0:
                c+=1
        if c==2:
            print(z)
            break
        c=0