#Write a function that takes a string consisting of alphabetic
#characters as input argument and returns the most common character.


def funkcja (string_1):
 string=string_1.lower().split()
 print (string)
 powtarzanie=[]
 y=0
 for x in range (0,len(string)):
  suma=0
  if string[y]:
   if x == string[y]:
    suma=suma+1
    y=y+1
    powtarzanie=powtarzanie.append(suma)
   if x!=string[y]:
     y=y+1
 return (powtarzanie) 

