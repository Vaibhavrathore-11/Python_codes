import random 

num = random.randint(1,101)
tries = 0
while True:
  guess = int(input("enter your guessing number :"))

  if num ==  guess:
    tries +=1
    print("you guess a right number {tries}, tries") 
    break

  elif num < guess:
    print("Go a littile lower")
    tries += 1


  elif num > guess:
    print("Go on littile higher")
    tries += 1

  else:
    print("invalid number")
    

