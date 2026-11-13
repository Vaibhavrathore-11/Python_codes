# Question -1 
#Given a tuple, print its total number of elements.

numbers = (10, 20, 30, 40, 50)

print(len(numbers))


# Question - 2
#ount how many times 20 appears in the tuple.

number = (10, 20, 30, 20, 40, 20, 50)
count = number.count(20)
print(count)



'''Q3. Find Maximum and Minimum

Find the largest and smallest elements without using max() and min().'''


number = (45, 12, 78, 23, 9, 56)

largest = max(number)

print("largest number:",largest)



num = (45, 12, 78, 23, 9, 56)

smallest = min(num)

print("smallest number:",smallest)


#Without max and min find a largest and smallest number

number = (45, 12, 78, 23, 9, 56)

largest = number[0]
smallest = number[0]

for i in number:
    if i > largest:
        largest = i

        if i < smallest:
            smallest = i

print("Largest number:", largest)
print("smallest number:",smallest)