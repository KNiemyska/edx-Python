#Write a function that accepts a list and returns
#a new list such that the new list contains
#all the items of the old list in reverse order.
#Note that this is NOT a sorting problem.
#Do NOT use the built in reverse() method for this problem
def funkcja(my_list):
 new_list=[]
 length=len(my_list)-1
 for x in range(length,-1,-1):
  new_list.append(my_list[x])
 return(new_list)
