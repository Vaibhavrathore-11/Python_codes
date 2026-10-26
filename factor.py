#Find the factor of n numbers

n = int(input("which number factorial you want"))

for i in range(1 , n+1):
    if n % i == 0:
     print(i)