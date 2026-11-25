Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> length = float(input("Enter the length: "))
Enter the length: 11
>>> width = float(input("Enter the width: "))
Enter the width: 4
>>> area = length * width
>>> Print("The area is", area, "square units.")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Print("The area is", area, "square units.")
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> Print("The area is", area, "square units.")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Print("The area is", area, "square units.")
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print("The area is", area, "square units.")
The area is 44.0 square units.
>>> length = float(input("Enter the length: "))
Enter the length: 8
>>> width = float(input("Enter the width: "))
Enter the width: 15
>>> area = length * width
>>> print("The area is", area, "square units.")
The area is 120.0 square units.
>>> length = float(input("Enter the length: "))
Enter the length: 8
>>> width = float(input("Enter the width: "))
Enter the width: 8
>>> area = length * width
>>> print("The area is", area, "square units.")
The area is 64.0 square units.
