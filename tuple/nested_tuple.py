number = (10,20,(30,40,50),60)

print(number[2])
print(number[2][2])
print(number[3])



name = ("vaibhav", "om",("ram", "divyansh","Lucky"),"kkkk")

print(name)



student = (
    ("Rahul" , 85, "A"),
    ("Aman", 21, "B"),
    ("om",22,"c")
)


print(student[0])
print(student[1][0])
print(student[2][0])


numbers = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(numbers[0])
print(numbers[1])
print(numbers[2])



# sum of all element
num = ((10, 20), (30, 40), (50, 60))
sum = 0

for i in num:
    for j in i:
     sum += j

print("Total sum:", sum)



# search for a number


numbers = ((10, 20, 30), (40, 50, 60), (70, 80, 90))

for i in numbers:
   for j in i:
      if j == 60:
         print("60 is found")




# count occurrences         

numbers = ((10, 20, 10), (30, 10, 40), (10, 50, 10))

count = 0

for i in numbers:
   for j in i:
      if j == 10:

         count += 1


print("10 appears", count, "times")