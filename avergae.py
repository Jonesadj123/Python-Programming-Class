def main():
    fileName = input("Enter the name of the file: ")

    with open(fileName, 'r') as file:
        numbers = list(map(float, file))

    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)

        print("The number of values in the file is:", len(numbers))
        print("The average is", round(average, 2))
    else:
        print("The file contains no numbers.")

if __name__ == "__main__":
    main()
