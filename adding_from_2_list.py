#Write a function that accepts two lists both of which consists of integers
#and returns the total sum of all the odd integers from both lists.

def funkcja (A,B):
 suma_A=0
 suma_B=0
 for x in range(0,len(A)):
  if A[x]%2!=0:
   suma_A=suma_A+A[x]
 for x in range(0,len(B)):
  if B[x]%2!=0:
   suma_B=suma_B+B[x]
 return (suma_A+suma_B)
