z=list(input().split())
b=[]
for i in z:
    for j in i:
        if j.isupper():
            b.append(j)
print(len(b))