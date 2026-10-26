# print all the factorial of the number first fall we take a user input

n = int(input("please tell your number :"))

fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"your factorial is {fact}")


