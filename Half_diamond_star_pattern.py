z=int(input())
a=z
if z>=3 and z<=100:
    for i in range(1,z*2):
        if i<=z:
            for j in range(1,i+1):
                print("*",end="")
        else:
            for k in range(1,a):
                print("*",end="")
            a-=1
        print()
else:
    print("The pattern is not possible")