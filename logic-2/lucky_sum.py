#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
    if a == 13 and b == 13:
        return 0
    if a == 13 and c == 13:
        return 0
    if a == 13:
        return 0
    if b == 13:
        return a 
    if c == 13:
        return a+b
    if a != 13 and b != 13 and c != 13:
        return a + b + c
