##Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
    """ if the numbers in an array of 2 contains 2 or 3 retunr True"""
    if nums[0] == 2 or nums[0] == 3:
        return True
    elif nums[1] == 2 or nums[1] == 3:
        return True
    else:
        return False

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))