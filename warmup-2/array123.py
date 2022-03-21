#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
    wewant = [1,2,3]
    for numbers in range(len(nums)):
        if nums[numbers: numbers+3] == wewant:
            return True
    return False