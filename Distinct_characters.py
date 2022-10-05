z=input()
d="".join(z)
b=set(d)
c=[]
op=""
for i in b:
    if i.islower():
        c.append(i)
e=sorted(c)
print("".join(e))
