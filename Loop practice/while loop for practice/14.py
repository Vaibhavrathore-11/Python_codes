# take a user input and reverse a number

n = int(input('Enter your number :'))

reverse = 0

while n > 0:
    num = n % 10
    reverse = reverse * 10 + num
    n = n // 10

print("Reverse number is", reverse)