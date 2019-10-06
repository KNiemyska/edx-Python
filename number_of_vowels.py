def total_number_of_vowels (input_string):
 number_of_vovels=0
 new_string=input_string.lower()
 vowels = ['a', 'e', 'i', 'o', 'u']
 for char in new_string:
  if char in vowels:
   number_of_vovels=number_of_vovels+1
 return number_of_vovels
