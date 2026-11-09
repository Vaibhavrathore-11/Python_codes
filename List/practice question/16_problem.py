#sum of even or odd numbers

numbers = [10,15,20,25,30,35,40]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num

    else:
        odd_sum = odd_sum + num

print("sum of even number is :",even_sum)
print("sum of odd number is :",odd_sum)


