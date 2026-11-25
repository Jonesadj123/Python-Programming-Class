Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Program: encrypt.py
... This program encrypts a line of text using a Caesar cipher. It asks the user for a line of plaintext and a distance value. It shifts each printable character by the distance entered.
... """
'\nProgram: encrypt.py\nThis program encrypts a line of text using a Caesar cipher. It asks the user for a line of plaintext and a distance value. It shifts each printable character by the distance entered.\n'
>>> plainText = input("Enter the plaintext: ")
Enter the plaintext: Hello World!
>>> distance = int(input("Enter the distance value: "))
Enter the distance value: 3
>>> encryptedText = ""
>>> for ch in plainText:
...     encryptedText += chr((ord(ch) - 32 + distance) % 95 + 32)
... 
>>> print("The encrypted text is:", encryptedText)
The encrypted text is: Khoor#Zruog$
