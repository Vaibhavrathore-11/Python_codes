#Student grading system
def get_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks! please enter marks between 0 to 100."
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 35:
        return "D"

    else:
        return "Fail"
print(get_grade(55))
print(get_grade(79))
print(get_grade(91))
print(get_grade(101))

