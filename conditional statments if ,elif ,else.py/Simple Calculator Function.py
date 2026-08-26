#Simple Calculator Function
 #operation parameter can have values ‘+’ , ‘-’ , '*’ & ‘/’ .
def calculator(a , b, operation):
    if operation == "+":
        return a + b 
    elif operation == "-":
        return(a - b)
    elif operation == "*":
        return(a * b)
    elif operation == "/":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    else:
        return "Error: Invalid operation"

print(calculator(10, 5, "+"))
print(calculator(35 , 7, "-") )
print(calculator(99,9, "*"))


        

