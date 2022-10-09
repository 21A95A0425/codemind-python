z=input()
m=input()
h=m.casefold()
g=z.casefold()
s=g.split(' ')
p=h.split(' ')
a=[]
for i in s:
    if i in p:
        if i not in a:
            a.append(i)
print(len(a))
        