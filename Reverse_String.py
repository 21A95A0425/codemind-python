z=input()
s=[]
for i in (z.split()):
    s.append(i)
k=len(s)
m=[]
for j in range(1,k+1):
    m.append(s[-j])
print(*(m))