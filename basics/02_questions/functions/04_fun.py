import math

def circle_stats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * (math.pi * radius) 
    return area, circumference

a, c = circle_stats(3) 


print(f"area is: {a:.2f}")
print(f"circumference is: {c:.2f}")