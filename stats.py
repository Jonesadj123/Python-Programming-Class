

def mean(numbers):
    """Return the average of the numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the middle value of the numbers."""
    if len(numbers) == 0:
        return 0

    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle - 1] +
                sorted_numbers[middle]) / 2


def mode(numbers):
    """Return the most frequently occurring number."""
    if len(numbers) == 0:
        return 0

    return max(set(numbers), key=numbers.count)


def main():
    """Test the statistical functions."""
    numbers = [4, 2, 7, 2, 9, 5, 2]

    print("Numbers:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))


if __name__ == "__main__":
    main()
