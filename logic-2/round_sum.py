#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

# def round10(num):
#     for i in range(num):
#         i += 1
#         i = 0
#         if i[-1] > 5:
#             return i[0] and 0
#         else:
#             return i[0] and 0


def round10(num):
    if num >= 5:
        return 10
    elif num
    elif num >= 15:
        return 20
    elif num

print(round10(15))



def round_sum(a, b, c):
    pass