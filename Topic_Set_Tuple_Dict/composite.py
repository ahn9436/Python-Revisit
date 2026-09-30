def composite(dict1, dict2):
    dict3 = {}

    for key, val in dict1.items():
        if val in dict2:
            dict3[key] = dict2[val]

    return dict3


dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

t = composite(dict1, dict2)
print(t)