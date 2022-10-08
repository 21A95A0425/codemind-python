z=input()
a=z.split()
n,m=0,0
for i in a:
    k=[]
    for j in i:
        k.append(ord(j))
    m+=max(k)
    n+=min(k)
print(abs(m-n))