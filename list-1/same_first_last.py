#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
    """if the array lenght s more than 1, this function says true if the first and last element of array are equal"""
    if len(nums) >= 1:
        return nums[0] == nums[-1]
    else:
        return False


print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))
print(same_first_last([]))