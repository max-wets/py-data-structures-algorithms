# Implement the _ _sub_ _ method for the Vector class of Section 2.3.3, so that the expression u—v returns a new vector instance representing the difference between two vectors.
# Implement the _ _neg_ _ method for the Vector class of Section 2.3.3, so that the expression −v returns a new vector instance whose coordinates are all the negated values of the respective coordinates of v. 
# In Section 2.3.3, we note that our Vector class supports a syntax such as v = u + [5, 3, 10, -2, 1], in which the sum of a vector and list returns a new vector. However, the syntax v = [5, 3, 10, -2, 1] + u is illegal. Explain how the Vector class definition can be revised so that this syntax generates a new vector. 
# Implement the _ _mul_ _ method for the Vector class of Section 2.3.3, so that the expression v * 3 returns a new vector with coordinates that are 3 times the respective coordinates of v. 
# Exercise R-2.12 asks for an implementation of _ _mul_ _, for the Vector class of Section 2.3.3, to provide support for the syntax v * 3. Implement the _ _rmul_ _ method, to provide additional support for syntax 3 * v.
# Implement the _ _mul_ _ method for the Vector class of Section 2.3.3, so that the expression u * v returns a scalar that represents the dot product of the vectors, that is, . 
# The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a parameter that is some iterable type representing a sequence of numbers, and to create a vector with dimension equal to the length of that sequence and coordinates equal to the sequence values. For example, Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these forms is acceptable; that is, if a single integer is sent, it produces a vector of that dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence. 

class Vector:
    """Represents a vector in a multidimensional space"""

    def __init__(self, d) -> None:
        """Creates a d-dimensional vector of zeros."""
        if isinstance(d, (int)):
            self._coords = [0] * d
        elif isinstance(d, list):
            self._coords = [0] * len(d)
            for j in range(len(d)):
                if not isinstance(d[j], int):
                    raise TypeError('coordinate must be an integer.')
                self._coords[j] = d[j]
        else:
            raise TypeError('parameter must be either an integer or a list of integers.')
        

    def __len__(self):
        """Returns the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Returns jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __neg__(self):
        """Return vector with negated values."""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __add__(self, other):
        """Returns sum of two vectors."""
        if len(self) != len(other):             # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))              # start with a vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, factor):
        """Return new vector with 'factor' times current coordinates."""
        result = Vector(len(self))
        if isinstance(factor, list):
            if len(factor) != len(self):
                raise ValueError('dimensions must agree')
            for j in range(len(self)):
                result[j] = self[j] * factor[j]          
        else:
            if not isinstance(factor, (int, float)):
                raise TypeError('The factor must be a numeric value')
            for j in range(len(self)):
                result[j] = self[j] * factor
        return result

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'      # adpat list representation

# v1 = Vector(5)
# for (i, x) in enumerate([0, 8, -3, 5, 10]):
#     v1.__setitem__(i, x)

# v2 = Vector(5)
# for (i, x) in enumerate([-2, 0, 4, 12, -4]):
#     v2.__setitem__(i, x)

# v = v1 + [5, 3, 10, -2, 1]
# print(v)

# u = [5, 3, 10, -2, 1] + v2

# print(v1)
# print(v1 * [3, 0, -10, 9, 4])
# print([3, 0, -10, 9, 4] * v1)
v3 = Vector(5)
print(v3)

v4 = Vector([8, -3, 7, 1, 0])
print(v4)

    