primeQ = 1419778561
staticY = 394137924
y = pow(staticY, 2, primeQ) * staticY
y = pow(y, 1, primeQ)
print("(y^3) mod primeQ =", y)

staticZ = 4360860
z = pow(staticZ, 1, primeQ)
for i in range(0, 511):
        z = pow(z * staticZ, 1, primeQ)
print("(z^512) mod primeQ =", z)
