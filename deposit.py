from authentication import acc_details
from utils import balance
def deposit():
    while True:
        x = int(input("Enter your ACCOUNT NUMBER: "))
        for key in acc_details.keys():
            if x == key:
                y = int(input("Enter PIN:"))

                if y == acc_details[x]:
                    z =int(input("Enter the amount:"))
                    balance[x] = balance.get(x, 0) + z
                    print("Money deposited Successful ")
                    print("Your account balance :", balance.get(x,0))
                    break
                else:
                    print("Invalid PIN")
                    deposit()
            else:
                print("Account Number Doesn't Exit")
                deposit()
        break
