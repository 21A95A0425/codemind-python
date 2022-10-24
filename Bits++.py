a=b=0
for i in range(int(input())):
    z=input()
    if "++" in z:
        a+=1
    if "--" in z:
        b+=1
print(a-b)