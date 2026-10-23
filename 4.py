#Accept a year and check if it a leap year or not . 

year = int(input("tell me  your years:"))

if year % 100 == 0 and year % 400 == 0:
    print("Its a leap year")
elif year% 100 !=0 and year % 4 == 0:
    print("Its a leap year")

else:
    print("Its normal year")