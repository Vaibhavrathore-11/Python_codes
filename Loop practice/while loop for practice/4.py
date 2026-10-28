# take a numberr from a user and count a total digit and print

a = int(input("enter your number"))

count = 0
while a > 0:
     count = count + 1
     a = a // 10

print("Total digits",count)


#Question 2

b = 3456789
count = 0
while b > 0:
    count = count + 1
    b = b // 10

print("sum of number is", count)