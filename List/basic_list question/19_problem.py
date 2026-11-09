"""Problem: Given a list of numbers and another list of new elements, insert each new element at the specified index.
Conditions:
- Use insert().
- Use a for loop.
- Don't use append() or create another list."""


numbers = [10,20,30,40,50]
new_numbers = [100,200,300]

for i in range(len(new_numbers)):
    numbers.insert(2 + 1 , new_numbers[i])

print(numbers)
