a=int(input())
for i in range(1,a+1):
    for j in range(1,1+a):
        if i==j or j==1 or j==a:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()