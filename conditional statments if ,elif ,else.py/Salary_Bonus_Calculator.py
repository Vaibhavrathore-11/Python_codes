'''Write a Python program that takes an employee's salary and years of experience as input and calculates the bonus based on the following conditions:

Experience 5 years or more → 20% bonus
Experience 3 to 4 years → 10% bonus
Experience 1 to 2 years → 5% bonus
Experience less than 1 year → No bonus

Finally, display the salary, bonus amount, and total salary after adding the bonus.'''


salary = float(input("Enter Your Salary:"))
Experience = int(input("Enter Your Experience of Year:"))

if Experience >= 5:
    bonous = salary * 0.20
elif Experience >= 3:
    bonous = salary * 0.10
elif Experience >= 1:
    bonous = salary * 0.05

else:
     bonous = 0 

print("Salary:",salary)
print("Bonous:",bonous)
print("Total Salary:", salary + bonous)       