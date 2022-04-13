#Return the number of times that the string "hi" appears anywhere in the given string.
#Got help from https://gregorulm.com/coding-bat-python-string-2/

def count_hi(str):
    hi = 'hi'
    counthi = 0
    for letters in str:
        if str(letters, letters +2) == hi:
            counthi += 1
    return counthi

