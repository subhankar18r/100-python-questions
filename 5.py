import cmath
import math
a,b,c = input("Enter a, b, c of a quadratic equation of the form ax^2+bx+c: ").split()
a = int(a)
b = int(b)
c = int(c)

discriminant = b**2 - (4*a*c)
 

if discriminant<0:
    x = (-b + cmath.sqrt(discriminant))/2*a
    y = (-b - cmath.sqrt(discriminant))/2*a
    print("Two complex roots are: ", x ," and ", y)
elif discriminant > 0:
    x = (-b + math.sqrt(discriminant))/2*a
    y = (-b - math.sqrt(discriminant))/2*a
    print("Two real roots are: ", x ," and ", y)
else:
    x = (-b + math.sqrt(discriminant))/2*a
    print("One real root is: ", x )
    

