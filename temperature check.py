# program to check whether condition based on temperature based on celsius

temp = int(input("Enter your temperature:"))

if temp < 0:
    print("Temperature is Freezing Cold")

elif temp >= 0 and temp < 10:
    print("Temperature is Very cold")

elif temp >=10 and temp < 20:
    print("Temperature is cold")


elif temp >=20 and temp <30:
    print("Temperature is Pleasant")

elif temp >=30 and temp <40:
    print("Temperature is Hot")

else : 
    print("Temperature is very Hot")