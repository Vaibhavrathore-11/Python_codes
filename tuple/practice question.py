#Q4. Find Second Largest Element

#Find the second-largest element without using sort() or sorted().


numbers = (10, 50, 30, 80, 60, 70 )

largest = numbers[0]
sec_largest = numbers[0]

for i in numbers:
    if i > largest:
        sec_largest = largest
        largest = i


    elif i >sec_largest:
        sec_largest = i

print("sec_largest is:",sec_largest) 
print("First largest is:", largest)


'''Q5. Separate Even and Odd Numbers

Create two separate tuples containing even and odd numbers.'''

numbers = (12,15,18,21,24,27,30)

even =()
odd =()

for i in numbers:
    if i % 2 == 0:
        even = even + (i,)

    else:
        odd = odd + (i,)


print("Even numbers:", even)
print("odd numbers:", odd)


#Q6. Find Common Elements

'''Find common elements between two tuples'''

a = (10,20,30,40,50)
b = (30,40,60,60,80)

common = []

for i in a:
    if i in b:
        common.append(i)

print(tuple(common))


# Remove duplicate element

num = [10,20,30,40,20,10,50]

unique = ()
for i in numbers:
    if i not in unique:
        unique = unique + (i ,)

print("original tuple",num)
print("unique tuple", unique)

