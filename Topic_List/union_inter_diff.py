def my_union(l1, l2):
    l3 = []
    for i in l1:
        l3.append(i)

    for j in l2:
        if j in l3: 
            continue
        else: 
            l3.append(j)

    print(l3)
    return l3

def my_intersection(l1, l2):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)

    print(l3)
    return l3

def my__difference(l1, l2):
    l3 = []
    for i in l1:
        if i in l2: continue
        else: l3.append(i)

    print(l3)
    return l3

list_1 = [3,6,8,4,6,11]
list_2 = [3,5,11,9,1,8,7,5,6]
my_union(list_1, list_2)
my_intersection(list_1, list_2)
my__difference(list_1, list_2)