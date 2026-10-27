def perm2(t, current=()):
    if len(current) == 2:
        print(current, end=" ")
        return
    
    for i in range(len(t)):
        remaining = t[:i] + t[i+1:]
        perm2(remaining, current + (t[i],))

def perm3(t, current=()):
    if len(current) == 3:
        print(current, end=" ")
        return

    for i in range(len(t)):
        remain = t[:i] + t[i+1:]
        perm3(remain, current + (t[i],))

def perm(t, n, current=()):
    if len(current) == n:
        print(current, end=" ")
        return

    for i in range(len(t)):
        remain = t[:i] + t[i+1:]
        perm(remain, n, current + (t[i],))


perm((1,2,3,4), 2)
print("")
print("")
perm2((1,2,3,4))
print("")
print("")
perm((1,2,3,4,5), 3)
print("")
print("")
perm3((1,2,3,4,5))
