a=input()
b="qwertyuioplkjhgfdsazxcvbnmQWERIOPLKJHGFDSAZXCVBNM1234567890"
n="1234567890"
c=0
e=[]
o,k=[],[]
for i in a:
    if i not in b:
        c+=1
for j in a:
    if j in n:
        if int(j)%2==0:
            e.append(j)
        else:
            o.append(j)
m=min(len(e),len(o))
if c%2==0:
    for l in range(0,m):
        print(e[l],end="")
        print(o[l],end="")
    if len(o)>len(e):
        print(o[-1],end="")
    elif len(o)<len(e):
        print(e[-1],end="")
        
if c%2!=0:
    for z in range(0,m):
        print(o[z],end="")
        print(e[z],end="")
    if len(o)>len(e):
        print(o[-1],end="")
    elif len(o)<len(e):
        print(e[-1],end="")