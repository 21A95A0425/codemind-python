n=int(input())
a=str(n)
b=1
c=""
for i in a:
    if i=="6" and b==1:
        c+="9"
        b=0
    else:
        c+=i
        
print(c)
