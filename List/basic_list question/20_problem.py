num = [10,20,30,40,50]
new_num = [100,200,300]

for i in range(len(new_num)-1,-1,-1):
    num.insert(2 , new_num)

print(num)