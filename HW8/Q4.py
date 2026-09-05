digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")
checksum = 0

while True:
    if digits.isdigit():
        if len(digits) == 9:
            break
        else: 
            print("to short or to long")
            digits = input("Enter the number of digits: ")
    else: 
        print("not a digit")
        digits = input("Enter the number of digits: ")

print("Your ISBN-10 number is", end=" ")
for i in range(1,10):
    checksum = int(digits[i-1]) * i + checksum
    print(digits[i-1], end="")
if checksum % 11 == 10:
    checksum = "X"
else: checksum = checksum % 11
print(checksum)

