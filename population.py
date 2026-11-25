Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> initial_population = int(input("Enter the initial number of organisms: "))
Enter the initial number of organisms: 400
>>> growth_rate = float(input("Enter the rate of growth: "))
Enter the rate of growth: 2
>>> growth_period = int(input("Enter the number of hours to achieve this rate: "))
Enter the number of hours to achieve this rate: 6
>>> total_hours = int(input("Enter the total number of hours: "))
Enter the total number of hours: 12
>>> population = initial_population
>>> for hours in range(growth_period, total_hours + 1, growth_period):
...     population = population * growth_rate
...     print("The total population lis:", population)
... 
The total population lis: 800.0
The total population lis: 1600.0
>>>  print("The total population is:", population)
...  
SyntaxError: unexpected indent
>>>      print("The total population is:", population)
...      
SyntaxError: unexpected indent
