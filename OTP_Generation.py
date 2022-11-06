z=input()
s=" "
for i in z:
    c=int(i)
    if c%2!=0:
        s+=str(c*c)
print(int(s))