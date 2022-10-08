z=input()
a=z.split()
b=[]
for i in a:
    for j in i:
        b.append(ord(j))
    m=max(b)
    n=min(b)
    b=[]
    print(abs(m-n),end=" ")