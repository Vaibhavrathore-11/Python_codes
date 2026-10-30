n = int(input("Enter your number :"))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit

    n = n // 10

print("sum of digit is", sum)