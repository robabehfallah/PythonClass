Num1 = float(input("enter first Number: \n"))
Num2 = float(input("enter Second Number: \n"))
Operation = input("what is the Operation? \n\
Operation list:\n\
\t\t Addition = +\n\
\t\t Subtraction = -\n\
\t\t Multiplication = *\n\
\t\t Division = \\\
\n")

if Operation == "*":
    print("Result= ",Num1*Num2)
elif Operation == "+":
    print("Result= ",Num1+Num2)
elif Operation == "/":
    print("Result= ",Num1/Num2)
elif Operation == "-":
    print("Result= ",Num1-Num2)
else:
    print("Operation not supported")
