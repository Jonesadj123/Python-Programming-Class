Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Program: copyfile.py
... This program copies the contents of one text file to another. It asks the user for the names of the two files, reads the first file, and writes the contents to the second file.
... """
'\nProgram: copyfile.py\nThis program copies the contents of one text file to another. It asks the user for the names of the two files, reads the first file, and writes the contents to the second file.\n'
>>> inputFile = input("Enter the input file name: ")
Enter the input file name:  first.txt
>>> outputFile = input("Enter the output file name: ")
Enter the output file name: second.txt
>>> with open(inputFile, "r") as file:
...      contents = file.read()
...      with open(outputFile, "w") as file:
...          file.write(contents)
... print("The file has been copied.")
SyntaxError: invalid syntax
>>> 
>>> print("The file has been copied.")
The file has been copied.
