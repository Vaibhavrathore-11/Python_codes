correct_pin = 1234
Balance = 100000

pin = int(input("Enter UPI PIN:"))
amount = float(input("Enter a withdrawal amount:"))

if pin != correct_pin:
    print("Incorrect pin")

elif amount <= 0:
    print("Invalide Amount") 

elif amount > Balance:
    print("Insufficient Balance") 

else:
    Balance = Balance - amount
    print("Withdrawal Succesful")
    print("Remaining Balance:", Balance)

    print("** Thankyou for Withdrawal **")          