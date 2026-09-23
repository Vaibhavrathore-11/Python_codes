#Repetition Tuples can be repeated using the '*' operator 

my_tuple = (1, 2, 3)
repeated = my_tuple * 2

print(repeated)


#Question 
'''Create a tuple containing 5 numbers. Use the tuple repetition operator to repeat the entire tuple 3 times.

Print the original tuple.
Print the repeated tuple.
Use len() to find the total number of elements after repetition.'''

tup = (2,3,4,6,7)
print(tup)

repeat = tup * 3
print(repeat)

print(len(repeat))




numbers = (10, 20, 30)
letters = ("A", "B")

repeate_number = (10,20,30)*3
print(repeate_number)
repeate_letters = ("A", "B")*2
print(repeate_letters)

final_tuple = repeate_number + repeate_letters
print(final_tuple)
print(len(final_tuple))

print(final_tuple.count(20))