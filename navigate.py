"""
Program: navigate.py
Allows the user to navigate lines of text in a file.
"""

def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        while True:
            print("The file has", len(lines), "lines.")
            line_number = int(input("Enter a line number (0 to quit): "))

            if line_number == 0:
                break
            elif 1 <= line_number <= len(lines):
                print(lines[line_number - 1], end="")
            else:
                print("Invalid line number.")

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
