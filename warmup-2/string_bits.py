#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

# def string_bits(str):
#     result = ''
#     for letters in len(str):
#         if letters % 2 == 0:
#             result = result + letters
#     print(result)

# string_bits('Hello')

def string_bits(str):
    result = ''
    for letters in range(0, len(str), 2):
        result += str[letters]
    return result

print(string_bits('Hello'))