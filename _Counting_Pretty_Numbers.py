z=int(input())
c=0
for i in range(1,z+1):
    a,b=map(int,input().split())
    for k in range(a,b+1):
        r=k%10
        if r==2 or r==3 or r==9:
            c+=1
    print(c)
    c=0