z=input()
#z=z.split()
#for g in z:
a=[]
b=[]
c=[]
d=''
j=0
#    l=0
for i in range(len(z)):
    if z[i].isalpha() or z[i].isdigit():
        a.append(z[i])
    else:
        b.append(i)
        c.append(z[i])
a.sort()
l=0
for k in range(len(z)):
    if k in b:
        d+=c[j]
        j+=1
    else:
        d+=a[l]
        l+=1
print(d,end=" ")