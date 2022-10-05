z=list(input().split())
h="".join(z)
c=[]
d=[]
op=""
for i in h:
    if h.count(i)==1:
        c.append(i)
for j in c:
    if j.islower():
        d.append(i)
print(len(d))