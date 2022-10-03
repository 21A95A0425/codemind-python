for i  in range(int(input())):
    x=int(input())
    z=0
    while x>=2**z:
        z+=1
    print((2**(z-1)-1))