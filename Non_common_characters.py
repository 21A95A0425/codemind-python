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
        if i not in p:
            if ' ' not in i:
                a.append(i)
    else:
        b.append(i)
for k in p:
    if k not in a:
        if ' ' not in k:
            if k not in s:
                a.append(k)
print(len(a))
        
    
