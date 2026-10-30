#Question: User se ek number input lo aur while loop ka use karke 1 se lekar n tak ke sabhi even numbers ka sum calculate karo.

n = int (input("Enter your number :"))

i = 1
sum = 0
while i < n:
    if i % 2 == 0:
      sum = sum + i
    i +=1

print("sum of number is",sum)


# print sum of 1to 70 numbers

i = 1
sum = 0

while i < 70:
   sum = sum + i
   i  += 1

print("sum of number is",sum)




#Question: User se ek number input lo aur while loop ka use karke 1 se lekar n number tak ke sabhi odd  numbers ka sum calculate karo

n = int(input("Enter your number:"))
i = 1
sum = 0

while i <=  n:
   if i % 2 != 0:
      sum = sum + i
   i += 1

print("sum =",sum)
   
