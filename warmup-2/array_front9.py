#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

# def array_front9(nums):
#     for numbers in nums:
#         if nums[0:4] == 9:
#             return True
#         else:
#             return False



def array_front9(nums):
    first4 = nums[0:4]
    for numbers in range(len(first4)):
        if first4[numbers] == 9:
            return True
    return False



print(array_front9([1, 2, 9, 3, 4]))