def bubble_sort(l1):
    l2 = l1
    for i in range(0, len(l2)-1):
        for j in range(0, len(l2) -1 ):
            if l2[j] > l2[j+1]:
                l2[j], l2[j+1] = l2[j+1], l2[j]
            else: continue
    print(l2)
    return l2

bubble_sort([3,2,9,7,8])
bubble_sort([5,8,9,1,8,6,9])
bubble_sort([3,3,4,7,8,1,7])