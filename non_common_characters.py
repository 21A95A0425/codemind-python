z=input()
m=input()
s=z.casefold()
p=m.casefold()
#p=g.split(' ')
#s=h.split(' ')
a=[]
b=[]
c=''
for i in s:
    if i not in p:
        if i not in a:
            if i.isalpha():
                a.append(i)
    else:
        b.append(i)
for j in p:
    if j not in s:
        if j not in a:
            if j.isalpha():
                a.append(j)
a.sort()
for k in a:
    c=c+k
print(c)
