'''Q7. Count Even Digits
Question: User se ek number input lo aur while loop ka use karke us number mein total even digits count karo.'''

n = int(input("enter your number: "))

count = 0

while n > 0:
  if (n % 10) % 2 == 0:
    count +=1

  n = n // 10

print("Total digits:",count)