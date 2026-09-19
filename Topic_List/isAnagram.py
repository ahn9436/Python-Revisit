def isAnagram(String1, String2):
    s3 = String1.replace(' ', '').lower()
    s4 = String2.replace(' ', '').lower()
    l1 = []
    l2 = []
    count = 0
    for i in range(0, len((s3))):
        l1.append(s3[i])
    for j in range(0, len(s4)):
        l2.append(s4[j])

    for b in range(0, len(l1)):
        if l1[b] in l2:
            count += 1
            l1[b] = 0

    if count == len(l2) or count == len(l1):
        return True
    else:
        return False

g = isAnagram("silent", "listen")
print(g)

h = isAnagram("World Cup", "Everybody Jump")
print(h)

e = isAnagram("Dormitory", "Dirty room")
print(e)

c = isAnagram("School master", "The classroom")
print(c)


