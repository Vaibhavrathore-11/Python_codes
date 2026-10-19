import pandas as pd

students = (
    ("Rahul", 21, "Python"),
    ("Aman", 22, "SQL"),
    ("Anshika", 20, "Python"),
    ("Radhe", 23, "Java")
)


df = pd.DataFrame(students)
print("Aman" in students)
print("Anshika" in students)
print(len(students))