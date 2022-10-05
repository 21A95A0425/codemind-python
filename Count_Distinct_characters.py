z=input()
d="".join(z)
b=set(d)
c=0
op=""
for i in b:
    if i.islower():
        c+=1
print(c)
