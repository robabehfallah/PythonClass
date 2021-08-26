P1 = {'reza', 'fatemeh', 'ali', 'narges'}
R1 = {'ali', 'narges', 'mahdiyeh', 'ziba'}
A1 = P1.intersection(R1)
print(len(A1))
B1=P1.union(R1)
print(B1)
C1 = R1-P1
print(C1)
