z=input()
m=input()
g=z.casefold()
h=m.casefold()
p=g.split(' ')
s=h.split(' ')
a=[]
b=[]
for i in s:
    if i in p:
        if i not in a:
            a.append(i)
    else:
        b.append(i)
print(*a)
