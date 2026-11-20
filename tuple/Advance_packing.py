# Advance unpacking (*operator)

number = (10,20,30,40,50)
a , b,*c = number

print(a)
print(b)
print(c)


#Extended Unpacking using 

num = (10,20,30,40,50)

a, b, *remaning = num

print(a)
print(b)
print(c)


first , *middle , last = (21,31,41,51,61,71)

print("first = ",first)
print("middle = ",middle)
print("Last = ",last)