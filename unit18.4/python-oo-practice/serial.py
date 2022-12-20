"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator"""

        self.start = start
        self.next = start

    def generate(self):
        """Return next serial"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number"""

        self.next = self.start

    def __repr__(self):
        """Provide a nicer appearance in debugging messages or in the console"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

