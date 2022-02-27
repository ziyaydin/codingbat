#Given a non-empty string like "Code" return a string like "CCoCodCode".

# def string_splosion(str):
#     place = -1
#     for letters in str:
#         print(str[0 + place])
#         place += 1

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result


