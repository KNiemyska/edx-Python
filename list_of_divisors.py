#Write a function that accepts a positive integer k
#and returns the list of all the divisors of k.
#Your list should include both 1 and k.
def funkcja (k):
 my_list=[]
 for x in range(1,k):
     if k%x==False:
         my_list.append(x)
 print (my_list)
