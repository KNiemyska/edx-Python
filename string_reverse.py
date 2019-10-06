
def funkcja (input_string):
 string_reverse=""
 for character in input_string:
    string_reverse=character.swapcase()+string_reverse
 return string_reverse
