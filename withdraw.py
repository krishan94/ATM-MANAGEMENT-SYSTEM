from authentication import acc_details
from utils import balance
def withdraw():
    while True:
        x = int(input("Enter your ACCOUNT NUMBER: "))
        for key in acc_details.keys():
            if x == key:
                y = int(input("Enter PIN:"))

                if y == acc_details[x]:
                    current_balance = balance.get(x, 0)
                    print("Your Account Balance:", current_balance)
                    z = int(input("Enter the amount:"))
                    if z > current_balance:
                        print("Insufficient balance!❌")
                    else:
                        balance[x] = current_balance - z
                        print(f"Withdraw Successful✅")
                        print(f"Available balance: {balance[x]}")
                    break
                else:
                    print("Invalid PIN")
                    withdraw()
            else:
                print("Account Number Doesn't Exit")
                withdraw()
        break