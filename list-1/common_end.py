#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
from operator import truediv


def common_end(a, b):
    """This function returns true if the arrays a and b have the same first or last element"""
    if a [0] == b[0] or a [-1] == b[-1]:
        return True
    else:
        return False

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))
