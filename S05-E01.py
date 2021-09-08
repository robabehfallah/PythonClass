X1 = int(input("Please Enter a numbre:"))
X2 = int(input("Please Enter a numbre:"))

if X1 < X2:
    for x in range(X1,X2):
        print(x)
elif X1 > X2:
    for x in range(X2,X1):
            print(x)
else: print(X1)

