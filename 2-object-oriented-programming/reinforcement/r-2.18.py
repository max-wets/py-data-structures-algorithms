class Progression:
    """Iterator producing a generic progression
    
    Default iterator produces the whole numbers 0, 1, 2,...
    """

    def __init__(self, start=0) -> None:
        self._current = start

    def _advance(self):
        """Update self._current to a new value

        This should be overriden by a subclass to customize progression.

        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current  # records current value to return
            self._advance()         # advance to prepare for next time
            return answer           # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_progression(self, n):
        """Print next n values of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):       # inherit from Progression
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0) -> None:
        """Create a new arithmetic progression

        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        """
        super().__init__(start)                 # initialize base class
        self._increment = increment

    def _advance(self):                         # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment

class GeometricProgression(Progression):       # inherit from Progression
    """Iterator producing an geometric progression"""

    def __init__(self, base=2, start=1) -> None:
        """Create a new geometric progression

        increment   the fixed constant multiplied to each term (default 2)
        start       the first term of the progression (default 1)
        """
        super().__init__(start)                 # initialize base class
        self._base = base

    def _advance(self):                         # override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *= self._base

class FibonacciProgression(Progression):
    """Iterator producing a Fibonacci progression"""

    def __init__(self, first=0, second=1) -> None:
        """Create a new Fibonacci progression

        first      the first term of the progression (default 0)
        second     the second term of the progression (default 1)
        """
        super().__init__(first)                 # start progression at first
        self._prev = second - first             # fictitious value preceding the first

    def _advance(self):                         # override inherited version
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


# Give a short fragment of Python code that uses the progression classes from Section 2.4.2 to find the 8th value of a Fibonacci progression that starts with 2 and 2 as its first two values.
print('Fibonacci progression with start values 2 and 2:')
FibonacciProgression(2, 2).print_progression(8)

# When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, how many calls to next can we make before we reach an integer of 263 or larger? 
print('Arithmetic progression with start value 0 and increment 128')
# ArithmeticProgression(128, 0).print_progression(72000000000000000)
