primeQ = 1419771931
staticZ = 1419771930
z = pow(staticZ, 1, primeQ)
for i in range(0, 511):
	z = pow(z * staticZ, 1, primeQ)
print("(z^512) mod primeQ =", z)

staticY = 683615825
y = pow(staticY, 2, primeQ) * staticY
y = pow(y, 1, primeQ) 
print("(y^3) mod primeQ =", y)
