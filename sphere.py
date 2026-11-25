Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """Analysis: This program calculates the diameter, circumference, surface area, and volume of a sphere.
... pseudocode:
... 1. Enter the radius.
... 2. Calculate the diameter.
... 3. Calculate the circumference.
... 4. Calculate the surface area.
... 5. Calculate the volume.
... 6. Display all four results.
... """
'Analysis: This program calculates the diameter, circumference, surface area, and volume of a sphere.\npseudocode:\n1. Enter the radius.\n2. Calculate the diameter.\n3. Calculate the circumference.\n4. Calculate the surface area.\n5. Calculate the volume.\n6. Display all four results.\n'
>>> import math
>>> 
>>> radius = float(input("Enther the radius: "))
Enther the radius: 5
>>> diameter = 2 * radius
>>> circumference = 2 * math.pi * radius
>>> surfaceArea = 4 * math.pi **2
>>> volume = (4 / 3) * math.pi * radius **3
>>> 
>>> print("The diameter is:", round(diameter, 2))
The diameter is: 10.0
>>> print("The circumference is:", round(circumference, 2))
The circumference is: 31.42
>>> print("The surface area is:", round(surfaceArea, 2))
The surface area is: 39.48
>>> print("The volume is:", round(volume, 2))
The volume is: 523.6
