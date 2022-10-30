s=input()
v='aeiouAEIOU'
z='0123456789'
vow=0
con=0
dig=0
sp=0
for i in s:
    if i in v:
        vow+=1
    elif i in z:
        dig+=1
    elif ' ' in i:
        sp+=1
    else:
        con+=1
print('Vowels:',vow)
print('Consonants:',con)
print('Digits:',dig)
print('White spaces:',sp)