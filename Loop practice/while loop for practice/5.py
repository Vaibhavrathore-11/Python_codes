# Accept a number and check if it is pallindromic number (if number and its reverse are equal)

a = int(input("Enter a number :"))
rev = 0
while a > 0:

    rev = rev * 10 + a % 10
    a = a// 10

print(rev)

if rev == rev:
    print("pallindronic number")
else:
    print("not a pallindronic number ")

