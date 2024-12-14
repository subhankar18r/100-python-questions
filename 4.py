import math

x,y,z = input("Enter 3 sides of triangle with a space separator: ").split()
x = int(x)
y = int(y)
z = int(z)

semiPerimeter = (x+y+z)/2

area = math.sqrt(semiPerimeter * (semiPerimeter -x)* (semiPerimeter -y)* (semiPerimeter -z) )

print("area of the triangle is: ", round(area,2))