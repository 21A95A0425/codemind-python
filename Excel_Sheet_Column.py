z=int(input())
s=""
while z:
    a=z%26
    if a==0:
        s+="Z"
        z=(z//26)-1
    else:
        s+=chr(64+a)
        z=z//26
print(s[::-1])