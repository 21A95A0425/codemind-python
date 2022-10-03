for i in range(int(input())):
    z=input()
    y=reversed(z)
    a=c=0
    for j in y:
        if j=="1":
            c+=2**a
        a+=1
    print(c)
   