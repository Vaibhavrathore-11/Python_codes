# use count function count()

string = "asdfghasgdfgh"
count = string.count("g")
print(count)


#count in list
numbers = [1,2,3,4,2,5,6,7,2,4,2,4,9,2]
count = numbers.count(2)
print(count)

#count in string 
name = "vaibhavRathore" 
str = name.count("a")
print(str)

#count help of user input

num = [1,2,3,4,5,6,3,5,6,3,5,5,5]
x = int(input("Enter number"))
print("number occurs" , num.count(x))