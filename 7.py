# sum of  natural numbers using for loop

n = int(input("please tell your number :"))

count = 0

for i in range(1,n+1):
    count = count+i

print(f"Your sum is{count}")