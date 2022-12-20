"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...

    def __init__(self, path):
        """Read the file (fl), show num of words"""

        fl = open(path)

        self.words = self.parse(fl)

        print(f"{len(self.words)} - num of words")

    def parse(self, fl):
        """Parse the file (fl)"""

        return [w.strip() for w in fl]

    def random(self):
        """Return a random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """find words and avoid blank lines and #"""

    def parse(self, fl):
        """Parse file (fl) and avoid blank lines and #"""

        return [w.strip() for w in fl
                if w.strip() and not w.startswith("#")]
