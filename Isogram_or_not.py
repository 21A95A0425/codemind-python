z=input().lower()
op=""
for i in z:
    if i not in op:
        op+=i
print(op==z)