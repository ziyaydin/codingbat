#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
#Got help from https://gregorulm.com/coding-bat-python-string-2/

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False