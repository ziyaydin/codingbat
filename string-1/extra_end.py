#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(str):
    str[-2:] + str[-2:] + str[-2:]

print(extra_end('ziya'))