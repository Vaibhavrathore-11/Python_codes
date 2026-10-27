n = int(input("please tell your number :"))

count = 0
for i in range(1,n+1):

    if n%i == 0:
     count = count + 1

print(count)

if count == 2:
   print("Your number is prime")
else:
   print("Your prime number is not prime")