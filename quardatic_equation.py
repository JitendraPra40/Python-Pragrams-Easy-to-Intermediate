import math
# ax^2 + bx + c = 0
# roots = (-b +- root(b**2 - 4*a*c))/2*a
def quadratic(a, b, c):
    d = (b**2 - 4*a*c)
    # real and distict roots
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print(f"The roots of the equation are: {x1:.0f}, {x2:.0f}")
    
    # real and equal roots
   
    elif d == 0:
        x1 = -b/(2*a)
        print(f"The roots of the equation are: {x1:.0f}")

    else:
        real_part = -b/(2*a)
        img = math.sqrt(abs(-d))/(2*a)  
        # abs() is used to get the absolute value
        print(f"The roots of the equation are: {real_part:.2f} + {img:.2f}i and {real_part:.2f} - {img:.2f}i")
    
a = float(input("Enter coofficient a: "))
b = float(input("Enter coofficient b: "))
c = float(input("Enter coofficient c: "))
quadratic(a, b, c)