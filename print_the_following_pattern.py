a=int(input())
if a>0:
    for i in range(1,a+1):
        b=0
        print(" "*(a-i),end="")
        for k in range(1,2*i):
            if k<i:
                print(i-k,end="")
            else:
                print(b,end="")
                b+=1
        print()