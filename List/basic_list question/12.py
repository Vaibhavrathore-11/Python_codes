#Take 5 numbers from the user and store only even numbers in a new list using append().

new_list = []
for i in range(5):
    num = int(input("Enter your number :"))
    if num % 2 == 0:
        new_list.append(num)

print("Even numbers in the list are:",new_list)



'''Take 5 student marks from the user and store them in a list. Print the total marks.'''
num = []
for i in range(5):
    n = int(input("Enter your marks: "))
    num.append(n)


print("Final list of marks:",sum(num))
