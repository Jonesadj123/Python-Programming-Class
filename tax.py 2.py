Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """Analysis: This program calculates income tax.
... pseudocode:
... 1. Enter gross income.
... 2. Enter number of dependents.
... 3. Calculate taxable income.
... 4. Calculate income tax.
... 5. Display income tax
... grossIncome = float(input("Enter the gross income: "))
... numDependents = int(input("Enter the number of dependts: "))
... taxableIncome = grossIncome - 1000 - (3000 * numDependents)
... print("The income tax is:", round(incomeTax, 2))
... """
'Analysis: This program calculates income tax.\npseudocode:\n1. Enter gross income.\n2. Enter number of dependents.\n3. Calculate taxable income.\n4. Calculate income tax.\n5. Display income tax\ngrossIncome = float(input("Enter the gross income: "))\nnumDependents = int(input("Enter the number of dependts: "))\ntaxableIncome = grossIncome - 1000 - (3000 * numDependents)\nprint("The income tax is:", round(incomeTax, 2))\n'
>>> Gross income: 50000
SyntaxError: invalid syntax
>>> Gross Income: 50000
SyntaxError: invalid syntax
>>> grossIncome = float(input("Gross income:"))
Gross income: 50000
>>> numDependents = int(input("Enter the number of dependents:"))
Enter the number of dependents: 2
>>> taxableIncome = grossIncome - 1000 - (3000 * numDependents)
>>> incomeTax = taxableIncome * 0.20
>>> print("The income tax is:", round(incomeTax, 2))
The income tax is: 8600.0
