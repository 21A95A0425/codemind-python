z=int(input())
for i in range(1,z+1):
    a=input()
    b=a[::-1]
    c=len(a)
    if a==b:
        if c%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print("NO")