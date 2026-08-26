def menu():
    print("Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


balance = 1000
print("Initial Balance =", balance)


menu()
command = int(input())
while command != 4:
    if command == 1:
        print("Balance :", balance)


    elif command == 2:
        dep = int(input("Please enter amount : "))


        while dep <= 0:
            print("Insufficient money")
            dep = int(input("Please enter amount : "))
        balance += dep


    elif command == 3:
        drawn = int(input("Please enter amount : "))


        while 0 > drawn or drawn > balance:
             print("Insufficient money")
             drawn = int(input("Please enter amount : "))
        balance = balance - drawn    


    menu()
    command = int(input())




