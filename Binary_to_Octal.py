for i in range(int(input())):
    y=reversed(input())
    s=a=0
    for i in y:
        if i=="1":
            s+=2**a
        a+=1
    z=oct(s)
    print(z[2:])