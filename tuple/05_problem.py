'''Create two tuples containing 5 fruits and 5 vegetables. Concatenate both tuples into a single tuple.

Then:

Print both original tuples.
Print the combined tuple.
Use len() to print the total number of items in the combined tuple.'''

Fruits = ("Apple", "Orange", "Gavava", "stawberry", "orenge")

Vegetables = ("Tomato","Cauliflower", "ladyfingure", "capsicum")

print(Fruits)
print(Vegetables)

#Print the combined tuple.
combined_tuple = Fruits + Vegetables
print(combined_tuple)

print(len(combined_tuple))