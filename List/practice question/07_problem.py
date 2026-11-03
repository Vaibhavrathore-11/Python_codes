# Find the second largest number in a list

num = [12,13,14,17,18]
largest = num[0]
sec_largest = num[0]

for i in num:
    if i > largest:
        sec_largest = largest
        largest = i

    elif i > sec_largest:
        sec_largest = i

print("The second largest number is:", sec_largest)



