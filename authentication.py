from utils import acc_details
def pin_auth():
    global acc_number, pin
    acc_number= int(input("Enter your account number: "))
    pin = int(input("Enter The Pin: "))
    acc_details.update({acc_number:pin})

    
