#Write a function that accepts two positive integers a and b
#(a is smaller than b)and returns a list that
#contains all the odd numbers between a and b
#(including a and including b if applicable) in descending order.

def funkcja (a,b):
 my_list=[]
 for x in range(a,b+1):
   if x%2!=0:
    my_list.append(x)
 print(my_list)
 my_list.reverse()
 print(my_list)
