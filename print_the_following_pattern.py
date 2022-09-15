a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if j==i or j==(a+1-i):
            print("x",end="")
        else:
            print(0,end="")
    print()