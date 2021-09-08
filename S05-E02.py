x=[]
while True:
    y = int(input('please entre a number: '))
    if y<0:
        break
    x.append(y)
print(x)
print(sum(x))
print(sum(x)/len(x)
