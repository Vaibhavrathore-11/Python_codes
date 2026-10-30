#Break Statment

for i in range(1,39,1):
    #print(i)
  if i == 25:
    break
  else:
    print(i)

    # break statment
#loop are continue only 7 steps becausew break statment are apply
    for i in range(12):
      if (i == 8):
        break
      print("5 x", i , "=",5*i)


    for i in range(67):
     if (i == 46):
      break
     print(i)


# Continue statment

for i in range (87):
  if (i == 65):
    continue # continue statment skip the rest of the loop statment yaha per 65 skip hoga
  print(i)



  for i in range(12):          
    if (i == 10):
     print("Skip the iteration")
     continue
    print("5x",i,"=", 5 * i)

"""5x 0 = 0
5x 1 = 5
5x 2 = 10
5x 3 = 15
5x 4 = 20
5x 5 = 25
5x 6 = 30
5x 7 = 35
5x 8 = 40
5x 9 = 45
Skip the iteration
5x 11 = 55"""


#break statment are used only 

for i in range(1,47):
  if (i == 26):
    print("Break statment are exicuted")
    break
  print(i)

# break statment are used and else statment are also used for cover a out of range condition

for i in range (1,78):
  if i == 98:
     print("Break statment are exicuted")
     break
  else:
    print("Break statment are not exicuted")
 

       