correct_username = "vaibhav rathore"
correct_password = "2005"

Username= (input("Enter your name:"))
password = (input("Enter your password"))

if Username == correct_username and password == correct_password:
    print("Login Successful")

elif Username == correct_username and password !=correct_password:
    print("Incorrect password")

else: 
    print("Invalid Username")
