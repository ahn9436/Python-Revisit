def int_to_binary(inte):
    if inte == 0:
        print("The number is 0")
        return None
    elif inte < 0:
        print("The number is negative")
        return None
    else:
        div_value = inte
        return_value = ""
        while div_value > 1:
            return_value = str(round(div_value % 2)) + return_value
            div_value = div_value // 2
        return_value = str(round(div_value % 2)) + return_value
        return return_value    

def binary_to_int(bina):
    if bina == None:
        print("Nothing to convert")
        return None
    return_value = 0
    for i in range(0,len(bina)):
        return_value += (2 ** i) * int(bina[-1 - i])
    return return_value    

int_input = int_to_binary(int(input("Enter a number : ")))
print(int_input)
bin_value = binary_to_int(int_input)
print(bin_value)

