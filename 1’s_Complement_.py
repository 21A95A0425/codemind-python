w=int(input())
x=bin(w)
y=(x[2:])
z=str(y)
f=""
for i in z:
    if i=="0":
        i="1"
        f+=i
    else:
        i="0"
        f+=i
q=int(f,2)
print(q)