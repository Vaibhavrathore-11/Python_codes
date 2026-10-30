#Number reverse karo aur count karo ki usmein kitne even aur kitne odd digits hain. Sirf while loop use karna

n = int(input("Enter your number :"))

original = n
reverse = 0

while n > 0:
    num = n % 10
    reverse = reverse * 10 + num

    n = n// 10

print("reverse number  is:",reverse)

if n % 2==0:
    print("Even number is ",num)

else:
    print("odd num is",num)
