##Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    """ if the lenght of array greater or equal to 2 add the first 2 elemnts
    if the lenght is less then 2 add everyhitng
    if lenght is 0 return 0"""
    if len(nums) >= 2:
        return sum([nums[0], nums[1]])
    elif len(nums) < 2:
        return sum(nums)
    elif len(nums) <= 0:
        return 0

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))