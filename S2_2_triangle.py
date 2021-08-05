a = int(input("enter first number? \n"))
b = int(input("enter Second number? \n"))
c = int(input("enter third number? \n"))

if (a+b > c) or (a+c > b) or (b+c > a):
    print("they can form a triangle")
else:
    print("they can not form a triangle")
