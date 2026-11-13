#immutable

a = (1,2,3,4,5,6)
#a[0] = 45  'tuple' object does not support item assignment
print(a)


# Duplicates allowed

b = (12,14,67,88,56,12,12)
print(b)
print(type(b))


name = ["ram","shyam","om","om"]

print(name)
print(type(name))

# orderd
a = (10,20,30,40,50)
print(a[0])
print(a[3])
print(a[1])


#Hetrogenious

a = ( 1,2,34.3,True,"hello")
print(type(a))
print(a)