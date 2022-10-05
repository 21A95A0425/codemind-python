a,b=map(int,input().split())
z=[]
e=[]
o=[]
e_sum,o_sum=0,0
for _ in range(a):
    z.append(list(map(int,input().split())))
for i in range(len(z)):
    if i%2==0:
        e.append(z[i])
for j in range(len(z)):
    if j%2==1:
        o.append(z[j])
for k in e:
    e_sum+=sum(k)
for l in o:
    o_sum+=sum(l)
print(e_sum,o_sum)
