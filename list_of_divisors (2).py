def find_integer_with_most_divisors(input_list):
 list=[]
 max_divisors=0
 max_divisors_x=0
 for x in input_list:

   for divisors in range (1,x+1):
    if x%divisors==0:
     list.append(divisors)
   length=len(list)

   if length>max_divisors:
    max_divisors=length
    max_divisors_x=x
 return max_divisors_x      
