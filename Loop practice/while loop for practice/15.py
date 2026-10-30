n = int(input("Enter your number :"))

original = n
reverse = 0


while n > 0:
    num = n % 10
    reverse = reverse * 10 + num

    n = n// 10

print("reverse number  is:",reverse)

if original == reverse:
     print("palindrome")

else:
     print("Not palindrome")