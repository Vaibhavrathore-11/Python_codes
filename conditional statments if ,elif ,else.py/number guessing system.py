secret_number = 78

while True:
     try:
        guess = int(input("Guess the number:"))
        if guess > secret_number:
            print("Too high")

        elif guess < secret_number: 
            print("Too low")

        else:
            print("correct!")
            break
     except ValueError:  
         print("Please enter a valid integer.") 

