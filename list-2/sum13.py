#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#WIPPPP
def sum13(nums):
    for i in len(nums):
        if i == 13:
            sum(nums[:i])
        else:
            return sum(nums)
