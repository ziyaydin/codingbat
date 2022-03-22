#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


def centered_average(nums):
    a = max(nums)
    b = min(nums)
    c = sum(nums) - a - b
    return c / (len(nums)-2)




print(centered_average([1, 2, 3, 4, 100]))