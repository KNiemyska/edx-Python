
def funkcja (input_string):
 string_reverse=""
 string=input_string.split()
 for character in string:
  length=len(character)
  for letter in range (length-1,-1,-1):
   string_reverse=string_reverse+character[letter]
 return string_reverse
