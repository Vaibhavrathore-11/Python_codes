# inpt a number of a user and seperate each digit of a number and print it on the new line

a = int(input("Enter your number : "))

while a > 0:
    print(a % 10)
    a = a // 10



    # take a user input and print a number one by one reverse order

    b = 74629

    while b > 0:
        print(b % 10)
        b = b // 10