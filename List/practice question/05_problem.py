# check if list is shorted or not


a = [12,13,14,15,16]

for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")



b = [22,34,24,26,27]
for i in range(len(b)-1):
    if b[i] < b[i+1]:
        continue

    else:
        print("Your list is not sorted") 
        break

else:
    print("Your list is sorted")   