a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==j or (j==a+1-i):
            print(a+1-i,end=" ")
        else:
            print(end=" ")
    print()