primeQ = 1419778561
staticY = 394137924
y = pow(staticY, 1, primeQ)
for i in range(0, 511):
	y = pow(y * staticY, 1, primeQ)
print("(y^512) mod primeQ =", y)

staticZ = 4360860
z = pow(staticZ, 2, primeQ) * staticZ
z = pow(z, 1, primeQ)
print("(z^3) mod primeQ =", z)
