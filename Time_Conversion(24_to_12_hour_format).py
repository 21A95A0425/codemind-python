s=input()
a=int(s[:2])
b=s[3:]
if a>=12:
    f=a-12
    if f==0:
        k='12'+':'+b+' '+'PM'
    elif f<10:
        k='0'+str(f)+':'+b+' '+'PM'
    else:
        k=str(f)+':'+b+' '+'PM'
elif a!=0:
    k=s+' '+'AM'
else:
    if a==0:
        k='12'+':'+b+' '+'AM'
print(k)