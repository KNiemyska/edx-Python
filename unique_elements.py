#Write a function that accepts an input list and returns
#a new list which contains only the unique elements
#(Elements should only appear one time in the list
  #and the order of the elements must be preserved as the original list. ).

def funkcja (input_list):
 input_list.sort()
 new_list=[]
 for x in range(-len(input_list),0):
  if input_list[x]!=input_list[x+1]:
   new_list.append(input_list[x])
 return (new_list)
#def funkcja(sample_list):
#    output_list = []
#    for items in sample_list:
#        if items not in output_list:
#            output_list.append(items)
#    return output_list
