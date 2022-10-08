z=input()
m=z.split()
a=[]
b=[]
for i in m:
    for j in i:
        a.append(j)
    a.sort()
    b=a[::-1]
    print(a[0],b[0],end=" ")
    a=[]
    b=[]