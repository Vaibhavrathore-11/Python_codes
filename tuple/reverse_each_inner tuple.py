#Q10. Reverse Each Inner Tuple


numbers = ((10, 20, 30), (40, 50, 60), (70, 80, 90))

result = ()

for i in numbers:
    num = i[::-1]

    result +=(num ,)


print(result)



'''Question: Given a nested tuple, reverse each inner tuple using a loop and slicing.'''



data = (("Python", "Java", "C++"),        ("Apple", "Mango", "Banana"),("Red", "Green", "Blue"))

reverse = ()

for i in data:
  num = i[::-1]
  result += (num ,)
    
    
print(result)