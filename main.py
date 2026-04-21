from authentication import pin_auth
from balance_check import check_ban
from deposit import deposit
from withdraw import withdraw
def atm_management():
    while True:
        print("\n Welcome To The ATM")
        print("\n 1. Check Pin Authentication💳 ")
        print("\n 2. Check Balance ")
        print("\n 3. Deposit money ")
        print("\n 4. Withdraw money ")
        print("\n 5. Exit: ")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            pin_auth()
        elif choice == 2:
            check_ban()
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            print("Thank You! Visit Again")
            break
        else:
            print("Invalid input!❌")

atm_management()

        
        
