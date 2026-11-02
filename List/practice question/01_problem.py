# Find the greatest element and print it index too.

l = [12,345,677,367,564,23,45,78]

largest = l[0]
index = 0

for i in l:
    if i > largest :
        largest = i
        index = l.index(i)

print(" your Largest element is {largest} at index {index} :".format(largest=largest, index=index))


# find the greatest element and print it index too.    

num = [12, 45, 23, 89, 34, 67]

largest = num[0]
index = 0

for i in num:
    if i > largest:
        largest = i
        index = num.index(i)

print(" your Largest element is {largest} at index {index} :".format(largest=largest, index=index))
        