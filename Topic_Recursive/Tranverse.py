def print_btree(tree, num=0):
    if tree is None:
        return
    if type(tree) != list:
        print(". " * num,str(tree))
        return
    val = tree[0]
    print(". " * num,str(val))
    
    if len(tree) > 1 and tree[1] != None:
        d = tree[1]
        if type(d) == list:
            for child in d:
                print_btree(child, num + 1)
        else:
            print_btree(d, num + 1)

print_btree([1, [[11, [111, 112]], [12, [121, [122, 1222]]],[1,[[121,121]]]]], 0)