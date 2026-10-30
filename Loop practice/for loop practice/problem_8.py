#print the sum of all even & odd numbers in a range

n = int(input("please enter your number :"))

even = 0
odd = 0
for i in range(1 , n+1):
    if i % 2 == 0: 
     even = even + i

    else:
       odd = odd + i
print(f"Your even or odd sum is {even},{odd} ")

    
