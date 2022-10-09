z=input()
m=input()
h=m.casefold()
g=z.casefold()
s=g.split(' ')
p=h.split(' ')
a,b,c,x,y,z,d=[],[],[],[],[],[],[]
for i in s:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
for j in a:
    if j not in b:
        c.append(j)
for k in p:
    if k not in x:
        x.append(k)
    else:
        y.append(k)
for v in x:
    if v not in y:
        z.append(v)
for y in c:
    if y in z:
        d.append(y)
print(len(d))
        
        