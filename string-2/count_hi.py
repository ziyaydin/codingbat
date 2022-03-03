#Return the number of times that the string "hi" appears anywhere in the given string.


def count_hi(str):
    hi = 'hi'
    counthi = 0
    for letters in str:
        if str(letters, letters +2) == hi:
            counthi += 1
    return counthi

