#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

from xxlimited import new


def missing_char(str, n):
    new_str = str[0 : n]
    new_str1 = str[n + 1: len(str)]
    return new_str + new_str1