s=input()
a=[]
b=[]
f=False
c=[]
for i in s:
    c.append(i)
    if i not in a:
        a.append(i)
    else:
        b.append(i)
for k in a:
    if k not in b:
        f=True
        for m in range(len(c)):
            if k in c[m]:
                print(m)
                break
        if k in c[m]:
            break
if f==False:
    print(-1)