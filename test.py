import random
import math

smallDecimal = float(input("Enter a small number: "))
# print(smallDecimal)
largeDecimal = float(input("Enter a large number: "))
# print(largeDecimal)

randomRadius = random.uniform(smallDecimal, largeDecimal)
# print(randomRadius)

pi = math.pi
volume = 4.0/3.0 * pi * randomRadius**3
# print(volume)

print("The volume of a sphere with radius, " + str(randomRadius) + ", is: " + str(volume))

# I used one of the radii from the prompt to check my math, just ignore or delete whats below

# testvolume = 4.0/3.0 * pi * 97.66289370137568**3
# print(testvolume)