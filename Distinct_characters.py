z=list(input().lower().split())
h="".join(z)
op=""
for i in h:
    if h.count(i)==1:
        op+=i
k=sorted(op)
l="".join(k)
print(l)