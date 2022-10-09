z=input()
m=input()
s=z.casefold()
p=m.casefold()
#3p=g.split(' ')
#=h.split(' ')
a=[]
b=[]
c=0
for i in s:
    if i not in a:
        if ' ' not in i:
            a.append(i)
    else:
        b.append(i)
for k in a:
    if k in p:
        c+=1
print(c)
