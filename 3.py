#Accept name and age from the user . Check if the user is a valid voter or not

name = input("Enter your name:")
Age = int(input("Enter your age:"))

if Age >= 18:
    print(f"  hello {name} you are valid voter")
else:
    print(f" hello {name} you are not valid voter")