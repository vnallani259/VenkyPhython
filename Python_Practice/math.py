from math import sqrt, sin, cos, pi
p_x = 100
p_y = 0
radians = 10 * pi/180
COS10 = cos(radians)
SIN10 = sin(radians)
x, y = eval(input("Enter initial satellite coordinates (x,y):"))
d1 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y))
x_old = x; 
x = x*COS10 - y*SIN10
y = x_old*SIN10 + y*COS10
d2 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y))
print("Difference in distances: %.3f" % (d2 - d1))
