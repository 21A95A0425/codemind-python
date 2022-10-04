def vowel(z,v):
    z=z.casefold()
    c=0
    count={}.fromkeys(v,0)
    for character in z:
        if character in count:
            count[character]+=1
            c+=1
    return c
    
z=input()
v="aeiou"
print(vowel(z,v))