# Name: Amarion Jones
# Semester: Second Semester
# Due Date: 10/23/26
# Instructor: Mark L Panger

# This program analyzes a text file and creates an analysis report.

import re
from collections import Counter
from pathlib import Path



def analyze_file():
    """Analyze a text file and write the results to an output file."""

    # Ask the user to enter the input file name.
    input_file_name = input(
        "Enter the name of the input file: "
    ).strip().strip('"')

    # Create a path to the input file.
    input_path = Path(input_file_name)

    # Create the output file name.
    output_path = input_path.with_name(
        "Analysis-" + input_path.name
    )

  

    try:
        # Open and read the input file.
        with input_path.open("r", encoding="utf-8") as input_file:
            file_contents = input_file.read()

        # Count lines and characters.
        line_count = len(file_contents.splitlines())
        character_count = len(file_contents)

        # Extract words containing letters only.
        words = re.findall(r"[A-Za-z]+", file_contents.lower())

        # Count all words and their frequencies.
        total_word_count = len(words)
        word_counts = Counter(words)

        # Calculate average word length.
        if total_word_count > 0:
            average_word_length = (
                sum(len(word) for word in words) / total_word_count
            )
        else:
            average_word_length = 0.0

        # Sort unique words alphabetically.
        unique_words = sorted(word_counts.keys())
        unique_word_count = len(unique_words)

        # Calculate average length of unique words.
        if unique_word_count > 0:
            average_unique_word_length = (
                sum(len(word) for word in unique_words)
                / unique_word_count
            )
        else:
            average_unique_word_length = 0.0

        # Count consecutive two-word pairs.
        word_pairs = Counter(
            (words[index], words[index + 1])
            for index in range(len(words) - 1)
        )

        # Keep pairs appearing more than once.
        repeated_pairs = sorted(
            (pair, frequency)
            for pair, frequency in word_pairs.items()
            if frequency > 1
        )

        repeated_pair_count = len(repeated_pairs)

        # Open the output file and write the report.
        with output_path.open("w", encoding="utf-8") as output_file:

            # Section 1: File statistics.
            output_file.write("FILE STATISTICS\n")
            output_file.write("----------------\n")
            output_file.write(f"Number of lines: {line_count}\n")
            output_file.write(f"Number of words: {total_word_count}\n")
            output_file.write(f"Number of characters: {character_count}\n")

            # Section 2: Unique words.
            output_file.write("\nUNIQUE WORDS AND FREQUENCIES\n")
            output_file.write("----------------------------\n")

            for word in unique_words:
                output_file.write(f"{word} ({word_counts[word]})\n")

            # Section 3: Repeated word pairs.
            output_file.write("\nREPEATED TWO-WORD PAIRS\n")
            output_file.write("-----------------------\n")

            for pair, frequency in repeated_pairs:
                output_file.write(f"{' '.join(pair)} ({frequency})\n")

            # Section 4: Summary statistics.
            output_file.write("\nSUMMARY STATISTICS\n")
            output_file.write("------------------\n")
            output_file.write(f"Total number of words: {total_word_count}\n")
            output_file.write(
                f"Average length of a word: {average_word_length:.2f} letters\n"
            )
            output_file.write(f"Number of unique words: {unique_word_count}\n")
            output_file.write(
                f"Average number of letters in unique words: "
                f"{average_unique_word_length:.2f}\n"
            )
            output_file.write(
                f"Number of repeated word pairs: {repeated_pair_count}\n"
            )

        # Display required information on the screen.
        print("\nFILE STATISTICS")
        print("----------------")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {total_word_count}")
        print(f"Number of characters: {character_count}")

        print("\nREPEATED TWO-WORD PAIRS")
        print("-----------------------")
        if repeated_pairs:
            for pair, frequency in repeated_pairs:
                print(f"{' '.join(pair)} ({frequency})")
        else:
            print("No repeated two-word pairs were found.")

        print("\nSUMMARY STATISTICS")
        print("------------------")
        print(f"Total number of words: {total_word_count}")
        print(f"Average length of a word: {average_word_length:.2f} letters")
        print(f"Number of unique words: {unique_word_count}")
        print(
            f"Average number of letters in unique words: "
            f"{average_unique_word_length:.2f}"
        )
        print(f"Number of repeated word pairs: {repeated_pair_count}")
        print(f"\nAnalysis report saved to: {output_path}")

    except OSError as error:
        print(f"File error: {error}")


# Start the program.
if __name__ == "__main__":
    analyze_file()
