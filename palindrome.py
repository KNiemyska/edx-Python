def palindrome (string):
 str.lower(string)
 palindrome_string=""
 for letter in string:
  palindrome_string=letter+palindrome_string
  print (palindrome_string)
  print (string)
 if palindrome_string==string:
  return True
 else :
  return False
