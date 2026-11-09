#use clear method to remove all elements
#from the list

list = [1,2,3,4,5]
list.clear()

print(list)


#index() method returns the index of the first matching element in the list

a = [10,20,30,40,30]

print(a.index(40))
print(a.index(30))


# count() method returns the number of times a specific element appears in the list

a = [10,60,30,10,10,20,60,70]

print(a.count(10))# 3
print(a.count(60))#2

