
#Given an array of ints, return the number of 9's in the array.


def array_count9(nums):
    amount_of_nine= 0
    for numbers in nums:
        if numbers == 9:
            amount_of_nine += 1
    return amount_of_nine
