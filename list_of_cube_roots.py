#Write a function that accepts a positive integer k
#and returns the ascending sorted list of cube root values
#of all the numbers from 1 to k (including 1 and not including k).
#[if k is 1, your program should return an empty list]
def funkcja(k):
 my_list=[]
 for x in range (1,k):
     a=k**x
     my_list.append(a)
 my_list.sort()
 print(my_list)
