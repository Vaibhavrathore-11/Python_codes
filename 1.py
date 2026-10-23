# Accept the gender from the user as char and print the respective greatting message 

gender = input("please tell your gender as character (M or F):")

if gender == "M" or gender == "m" :
    print("Good Morning Sir")
elif  gender == "F" or gender == "f":
    print("Good morning mam have a nice day")
else:
    print("unidentified gender")