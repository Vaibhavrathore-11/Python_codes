
# using while loop and print 1 to 10 numbers

i = 0

while i <= 19:
    i += 1
    print(i)

    # print even numbers

    i = 2
    while i <  20:
        if i % 2 == 0:
            i+=2
            print(i)


        # using While loop and print reverse order in string 10 to 1
i = 10
while i >= 1:
   print(i)
   i -=1

# . Sum of numbers

#1 se 10 tak sabhi numbers ka sum nikalo.

i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i+= 1
    print(i)

print("Total sum:",sum)



# print sum of number 1 To 50

i = 1
sum = 0

while i <= 50:
    sum = sum + i
    i += 1
    print(i)

print("Total sum:", sum)


# take a user input and sum of number 

n = int(input("Enter your number:"))

i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1

print("sum of number is", sum)