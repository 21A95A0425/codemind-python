from math import*
z=int(input())
mat1=[]
mat2=[]
op=[]
ip=[]
for _ in range(z):
    mat1.append(list(map(int,input().split())))
for _ in range(z):
    mat2.append(list(map(int,input().split())))
for i,j in zip(mat1,mat2):
    for k,l in zip(i,j):
        op.append(abs(k-l))
x=int(len(op)//sqrt(len(op)))
y=0
for ii in range(x):
    xp=op[y:x]
    ip.append(xp)
    y=x
    x+=int(sqrt(len(op)))
for i in ip:
    print(*i)