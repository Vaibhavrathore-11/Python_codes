'''Write a Python program that creates a list of numbers and takes a number from the user. Remove that number from the list using the remove() function and print the updated list.
Original list: [10, 20, 30, 40, 50]
Enter number to remove: 30
Updated list: [10, 20, 40, 50]'''

Original_list =  [10, 20, 30, 40, 50]

updated_list = Original_list.remove(30)

print(Original_list)


#Question - 2

Fruits = ["Apple" , "Banana", "orange", "Mango" , "Kiwi"]
print(Fruits)

fruit = Fruits.remove("orange")
print(Fruits)