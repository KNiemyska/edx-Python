#Write a function that accepts two positive integers a and b
#and returns a list of all the even numbers between a and b
#(including a and not including b).

def funkcja (a,b):
 my_list=[]
 for x in range(a,b):
   if x%2==0:
    my_list.append(x)
 print(my_list)
