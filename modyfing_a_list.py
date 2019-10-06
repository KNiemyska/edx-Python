def funkcja (my_list):
 a=[]
 length=len(my_list)
 for x in range (0,length):
  if my_list[x]%2==0:
   a.append(my_list[x])
  else:
   a.append(my_list[x]+1)
 return (a)
