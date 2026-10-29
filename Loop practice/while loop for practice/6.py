# Generate a random number

import random 

num = random.randint(1 , 11)
print(num)
guess = int(input("Please guess your number :"))

if num == guess:
    print("you are right")

else:
    print("sorry You are wrong")


#  make a random guessing game

import random

num = random.randint(1,11)
tries = 0
while True: 
  guess = int(input("Enter your guess number"))

  if num == guess:
    tries +=1
    print("you are right you guessed the number is  {tries},tries ")
    break

  elif num < guess:
     print("Go a littile lower")
     tries += 1

  elif num > guess:
     print("Go a little higher ")
     tries += 1

  else:
     print("Sorry you are wrong")