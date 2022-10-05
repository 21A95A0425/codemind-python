def pangram(z):
    a="qwertyuiopasdfghjklzxcvbnm"
    for i in a:
        if i not in z.lower():
            return False
    return True
print(pangram(input()))