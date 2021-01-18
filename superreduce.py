

def superReducedString(s):
    i = 0
    
    while s[i] == s[i + 1]:
        s = s - (2*s[i])
        i += 1
        if i += 1 >= len(s):
            i = 0