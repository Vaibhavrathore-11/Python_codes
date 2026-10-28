#print 1 to 100 numbers
for i in range(1,101,1):
    print(i)

    # print 1 to 50 even numbers
    for i in range (1,51):
        if i % 2 == 0:
            print(i)


# print multiplication table of number
num = int(input("Enter your number :"))
for i in range(1,11,1):
      print(num, "x",i, "=", num * i)