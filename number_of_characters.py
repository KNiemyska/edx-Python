def number_of_characters (input_string, character):
 number_of_vovels=0
 new_string=input_string.lower()
 for char in new_string:
  if char ==character:
   number_of_vovels=number_of_vovels+1
 return print(number_of_vovels)
