Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Program: decrypt.py
... This program decrypts a line of encrypted text using a Caesar cipher. It asks the user for encrypted text and a distance value. It shifts each printable character backward by the distance entered.
... """
'\nProgram: decrypt.py\nThis program decrypts a line of encrypted text using a Caesar cipher. It asks the user for encrypted text and a distance value. It shifts each printable character backward by the distance entered.\n'
>>> encryptedText = input("Enter the encrypted text: ")
Enter the encrypted text: Khoor#Zruog$
>>> distance = int(input("Enter the distance value: "))
Enter the distance value: 3
>>> plainText = ""
>>> for ch in encryptedText:
...     plainText += chr((ord(ch) - 32 - distance) % 95 + 32)
... 
>>> print("The plaintext is:", plainText)
The plaintext is: Hello World!
