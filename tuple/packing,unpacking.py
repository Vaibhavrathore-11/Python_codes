#  Packing: Multiple values and data types in a one tuple

a = (12,45,2.34,"gopi","harsh", True,)
print(a)

b = ("vaibhav", 23 , 2.3, "B.tech")

print(b)

# unpacking - Tuple element and value store in a diffrent variables

student = ("vaibhav",21,6.65,"B.tech")

name ,  age , cgpa , course = student

print(name)
print(age)
print(cgpa)

#basic unpacking
num = (10,20,30,40)

a,b,c,d = num

print(a)
print(b)
print(c)

# List unpacking

student = ["boy",20,8.82]

name, age, cgpa = student

print(name)
print(age)
print(cgpa)


# Advanced packing

num = (122,133,144,155)

a,b,*c= num
print(a)
print(b)
print(c)


#Question -2
number = (10,20,30,40)
a, *b = number
print(a)
print(b)


