print("Secure code execution Started")
print("Welcome to Bank Of Manipal")

balance = 10000
print("A. Check Balance /n B. Withdraw /n C. check the loan intrest rate")
opt = input("Enter your option: ")
if opt == 'A':
    print("Your account balance is:", balance)
elif opt == 'B':
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("Withdrawal successful. New balance is:", balance)
    else:
        print("Insufficient funds.")
elif opt == 'C':
    try:
        p = float(input("Enter the principal amount: "))
        t = float(input("Enter the time in years: "))
        r = float(input("Enter the rate of interest: "))
    except Exception:
        print("Invalid input. Please enter numeric values.")
        print("Thank you for using Bank Of Manipal services")
        exit()
    
    si = (p * t * r) / 100
    print("The simple interest is:", si)
else:
    print("Invalid option selected.")
    print("Thank you for using Bank Of Manipal services")
    exit()
     