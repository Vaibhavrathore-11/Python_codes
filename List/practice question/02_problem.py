list = [1,2,3,4,5,6]

list[2] = 38

print(list)

#Question - print positive and negative numbers from the list

l = [1,-2,3,-45,-65,7,-84]

print("positive elements in the list are :")
for i in l:
    if i >=0:
        print(i)


print("negative elements in the list are :")
for i in l:
    if i < 0:
     print(i)