#Q1. Tax Calculator based on Salary
#• If salary < 30,000 → 5%
#• If salary is 30,000–70,000 → 15%
#• If salary > 70,000 → 25%

salary = float(input("Enter your salary:"))

if salary < 30000:
    tax_rate = 5

elif 30000 <= salary <= 70000:
    tax_rate = 15

else:
    salary > 70000
    tax_rate = 25

print(f"Tax Rate: {tax_rate}%")    