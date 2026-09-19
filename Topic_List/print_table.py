def print_table(l1):
    max = [0] * len(l1[0])

    for b in range(0, len(l1[0])): #2
        for c in range(0, len(l1)): #4
            if max[b] > len(str(l1[c][b])): continue
            max[b] =(len(str(l1[c][b])) + 2)


    for i in range(0, len(l1)):
        for j in range(0, len(l1[i])):
            print(f"{l1[i][j]:<{max[j]}}", end="")
        print("")


# print_table([["X","Y"], [0,0], [10,10], [200,200]])
# print_table([["ID","Name","Surname"],
#              ["001","Guido","van Rossum"], 
#              ["002", "Donald", "Knuth"], 
#              ["003", "Gordon", "Moore"] ])

print_table([["Name", "Power", "Health"], 
             ["Wolf", "50", "100"], 
             ["Skeleton", "150", "50"],
             ["Mouse", "10", "10"]])