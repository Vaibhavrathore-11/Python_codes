#User se ek number input lo aur while loop ka use karke us number mein total odd digits count karo.

n = int(input("Enter your number :"))

count = 0

while n > 0:
    if (n % 10 )% 2 !=0:
        count +=1 # Count increase karna.

    n = n // 10 #Last digit remove karna.

print("odd count is",count)




"""n % 10 → Last digit nikalna.
% 2 != 0 → Odd digit check karna."""