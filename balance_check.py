from authentication import acc_details
from utils import balance
def check_ban():
    while True:
        x = int(input("Enter your ACCOUNT NUMBER: "))
        for key in acc_details.keys():
            if x == key:
                y = int(input("Enter PIN: "))

                if y == acc_details[x]:
                    print("Your Account Balance:", balance.get(x, 0))
                    
                else:
                    print("Invalid PIN")
                    check_ban()
                    
            else:
                print("Account Number Doesn't Exit")
                check_ban()
        break