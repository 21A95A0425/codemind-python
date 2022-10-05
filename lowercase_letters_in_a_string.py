z=list(input().split())
b=[]
for i in z:
    for j in i:
        if j.islower():
            b.append(j)
print(len(b))