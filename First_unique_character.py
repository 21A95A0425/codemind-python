z=input()
h="".join(z)
c=[]
k=0
op=""
for i in h:
    if h.count(i)==1:
        c.append(i)
        k=1
if k==0:
    print(-1)
else:
    print(c[0])
