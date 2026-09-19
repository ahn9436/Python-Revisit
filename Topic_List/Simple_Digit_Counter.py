string_input = input("Enter a String : ")

def digit_counter(inp):
    l1 = [0,0,0,0,0,0,0,0,0,0]
    num = [0,1,2,3,4,5,6,7,8,9]
    for i in range(0, len(string_input)):
        if string_input[i].isdigit():
            if int(string_input[i]) in num:
                l1[int(string_input[i])] += 1
            else: continue
        else: continue
    return l1

test = digit_counter(string_input)

for t in range(0,len(test)):
    if test[t] == 0: continue
    else:
        print(f"{t} occurs {test[t]} time")