z=int(input())
y=list(map(int,input().split()))
x=2**z
for i in range(x):
    a=[]
    b=bin(i)[::-1]
    for k in range(len(b)):
        if b[k]=="1":
            a.append(y[k])
    print(*a)
    a=[]