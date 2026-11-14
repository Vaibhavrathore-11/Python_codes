#Q1. Extract First and Last Elements

#Given a tuple, create a new tuple containing the first 2 and last 2 elements.

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

result = numbers[:2] + numbers[-2:]

print(result)



#Q2. Reverse Every Second Element

#Reverse the tuple and print every second element.

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

reverse = (numbers[::-1] [::2])
print(reverse)



'''Q3. Extract Middle Elements

Extract the middle 4 elements using slicing.'''

numbers = (5, 10, 15, 20, 25, 30, 35, 40)

num = numbers[2:6]
print(num)

'''Q4. Split a Tuple into Two Halves

Divide the tuple into two separate tuples using slicing.'''

numbers = (11, 22, 33, 44, 55, 66, 77, 88)

num1 = numbers[0:4]
num2 = numbers[4:]

print(num1)
print(num2)


'''Q5. Extract Elements at Odd Index Positions

Use slicing to extract elements present at odd index positions.'''

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

num = numbers[1:80:2]

print(num)