# check your input is palidrom are not

a = "madam"
b = ""
for i in range(-1,-6,-1):
   b = b + a[i]

if b == a:
       print("Your string is pallindrome")

else:
       print("Your string is not a pallindrome")






a = (input("check your pallindrom :"))



for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if b == a:
            print("Your number is pallindrome")
else:
            print("Your number is not a pallindrome")



a = "sdfgh#@@#$%^"

char = 0
dig = 0
spchar = 0

for i in a:
        if i .isdigit():
                dig +=1
        elif i.isalpha():
                char += 1
        else:
             spchar += 1
             print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchar}")