#Write a function named list_of_primes that accepts a positive
#integer n and returns a sorted list (ascending order) of all the prime numbers
#between 2 and n (including 2 but not including n)
def funkcja (integer):
 list_of_primes=[]
 for prime in range (2,integer+1):
  list=[]
  divisor=1
  while divisor<prime+1 :#czy prime jest liczbą pierwszą(liczba z 2 do integer)
   if prime%divisor==0:
    list.append(divisor)
    length=len(list)
   divisor=divisor+1
  if length==2:
   list_of_primes.append(prime)
 return (list_of_primes)
            
 
