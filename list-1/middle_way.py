##Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
    """this function takes the middle value of 2 different arrays of lenght 3 and returnts the middle value"""
    return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))