balance = 50000
withdraw = int(input("Enter Withdraw Amount:"))

if withdraw <= balance:
    balance -= withdraw
    print("Transiction succesfully")
    print("Remaining Balabce" , balance)

else:
    print("Insufficient Balance")