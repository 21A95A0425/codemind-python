z=int(input())
for i in range(1,z+1):
    for j in range(1,1+z):
        if i==z:
            print("*",end="")
            continue
        if i==j or j==1:
            print("*",end="")
        else:
            print(end=" ")
    print()