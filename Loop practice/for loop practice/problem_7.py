#Accept an integer and print hello world n times

n = int(input("please tell your number :"))

for i in range(n):
    print("hello World")


    ''' print natural number up to n

    n = int(input("please tell your number :"))

    for i in range(1, n+1):
        print(i)'''

    # print natural number n to 1

    n = int(input("please tell your number: "))

    for i in range(n , 0,-1):
        print(i)

        # Take a number as input and print its table

        n = int(input("which table you want :"))
        for i in range(1,11):
            print(f"{n}*{i} = {n* i}")
            print(n)