def print_upper_words(words, must_start_with):
    """Print out each word if starts with defined letter on a separate line, but in all uppercase"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words(["aAa", "bBb", "Aa", "Bb"], ["A", "B"])
