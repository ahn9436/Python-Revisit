def product(*s):
    res = set()

    for i in s[0]:
        res.add((i,))

    for j in s[1:]:
        n_res = set()
        for tup in res:
            for c in j:
                n_res.add(tup + (c, ))

        res = n_res
    return res

s1 = {1, 2, 3}
s2 = {'p', 'q'}
s3 = {'a', 'b', 'c'}

p1 = product(s1, s2, s3)
print(p1)