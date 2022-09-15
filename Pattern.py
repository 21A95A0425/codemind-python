a=int(input())
if a>0:
    for i in range(1,a+1):
        z=0
        print(" "*(a-i),end="")
        j=2
        for k in range(1,2*i):
            if k<=i:
                print(k,end="")
            else:
                print(k-j,end="")
                j+=2
        print()