Name = input("Please enter your name:")
Surname = input("PLease enter your surname:")
Age = int(input("Please enter your age:"))
Date = int(input("Please enter your birthday(just year):"))


list = [Name , Surname , Age , Date]

for i in list:
    print(i)



if Age < 18:
   print("You can't go out because it's too dangerous!")
elif Age >= 18:
   print("You can go out to the street. :D")
      