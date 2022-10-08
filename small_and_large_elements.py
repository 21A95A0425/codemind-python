z=input()
m=z.split()
a=m[0]
m=m[::-1]
b=m[0]
g=[]
h=[]
for i in a:
    g.append(i)
for j in b:
    h.append(j)
g.sort()
h.sort()
h=h[::-1]
print(g[0],h[0])