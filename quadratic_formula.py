import math
aVal = int(input("a value input:"))
bVal = int(input("b value input:"))
cVal = int(input("c value input:"))

discriminantFormula = bVal**2 - 4*aVal*cVal

if discriminantFormula > 0:
    print("the discriminant has two real roots")
    print(-bVal + math.sqrt(bVal**2 - 4*aVal*cVal)/(2*aVal))
    print(-bVal - math.sqrt(bVal**2 - 4*aVal*cVal)/(2*aVal))
elif discriminantFormula == 0:
    print("The discriminant has one real root")
    print((-bVal)/2*aVal)
else:
    print("The discriminant has no real roots")