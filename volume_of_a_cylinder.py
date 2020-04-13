import math
radius_of_cylinder = int(input())
height_of_cylinder = int(input())

volume = math.pi*radius_of_cylinder**2*height_of_cylinder

print(round(volume, 1))