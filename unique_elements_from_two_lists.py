#Write a function that accepts two input lists and returns
#a new list which contains only the unique elements from both lists.
def funkcja(sample_list,sample_list_2):
 sample_list.extend(sample_list_2)
 output_list = []
 for items in sample_list:
  if items not in output_list:
   output_list.append(items)
 return output_list
