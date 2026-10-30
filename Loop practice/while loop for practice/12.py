#User se ek number input lo aur while loop ka use karke us number ke sabhi digits ka sum calculate karo.

n = int(input("Enter your number :"))

sum = 0


while n > 0:
  digit = n % 10
  sum = sum + digit
  n = n // 10

print("sum of number is",sum)