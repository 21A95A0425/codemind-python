a=input()
b=[]
c=[""]
d=["a","e","i","o","u"]
for i in a:
    b.append(i)
for j in b:
    if j not in d:
        if c[-1]!="C":
            c.append("C")
    else:
        if c[-1]!="V":
            c.append("V")
for i in c:
    print(i,end="")
    