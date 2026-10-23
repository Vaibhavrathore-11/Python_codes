# number validator using if - elif - else

num = int(input("Enter Your Number:"))

if num > 0 and num <= 100:
    print("Number is Valid")

elif num> 100:
    print("num is too high")

else:
    print("Invalid Number")