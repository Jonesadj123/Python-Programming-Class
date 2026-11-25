Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> height = float(input("Enter the initial height: "))
Enter the initial height: 10
>>> bounces = int(input("Enter the number  of bounces: "))
Enter the number  of bounces: 2
>>> bounciness = 0.6
>>> total_distance = height
>>> for i in range(bounces):
...     height = height * bounciness
...     total_distance += height
...     if i < bounces - 1:
...         total_distance += height
... print("The total distance traveled is:", total_distance)
SyntaxError: invalid syntax
>>> print("The total distance traveled is:", total_distance)
The total distance traveled is: 10.0
>>> height = float(input("Enter the initial height: "))
Enter the initial height: 10
>>> bounces = int(input("Enter the number  of bounces: "))
Enter the number  of bounces: 2
>>> bounciness = 0.6
>>> total_distance = height
>>> for i in range(bounces):
...     height = height * bounciness
...     total_distance += height
...     if i < bounces - 1:
...         total_distance += height
...         print("The total distance traveled is:", total_distance)
... 
...     
The total distance traveled is: 22.0
