a=int(input())
if a>0:
    for i in range(1,a+1):
        print(" "*(a-i),end="")
        for k in range(1,2*i):
            print(i,end="")
        print()