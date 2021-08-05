a = int(input("enter first side's length? \n"))
b = int(input("enter Second side's length? \n"))
c = int(input("enter third side's length? \n"))

if (a+b > c) and (a+c > b) and (b+c > a):
    print("they can form a triangle")
else:
    print("they can not form a triangle")
