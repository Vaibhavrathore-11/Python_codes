#triangle_validity_checker

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if  a<= 0 or b <=0 or c<=0 :
    print("Invalid Triangle")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")

elif a==b or b==c :
    print("Equilateral triangle")

elif a==b or b==c or a==c :
    print("Isoscales Triangle")

else:
    print("Scalene triangle")