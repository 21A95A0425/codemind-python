z=input()
a=z.split()
b=[]
for i in z:
    if " " not in i:
        b.append(ord(i))
m=max(b)
n=min(b)
for j in z:
    if ord(j)==n:
        print(j,z.count(j),end=" ")
        break
for k in z:
    if ord(k)==m:
        print(k,z.count(k))
        break