#Tuple is a immutable does not change directly ones create

a = (1,2,3)
print(type(a)) # <class 'tuple

#How to print 1 element in tuple

b = (1,)
#print(type(b)) # output may be int because does not use (,)
print(type(b))

t = (12,14,55,64,43.3, False, "elon")
print(type(t))
print(t)
#t[0] = 122 does not change value because tuple are immutable you can create a new tuple 
#print(t)