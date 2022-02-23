#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) > 1:
        return str[-1] + str[1: len(str)-1] + str[0]
    elif len(str) <= 1:
        return str

print(front_back('code'))
print(front_back('babson'))


