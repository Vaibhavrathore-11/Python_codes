#check if list is shorted or not

a = [21,23,24,25,26,27,34]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list are not sorted")
        break
else:
    print("your list are sorted")