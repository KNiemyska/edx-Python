# Type your code here
n=int(input("the total numbers of hours the user worked in a week"))
if n<=40 and n>0 :
    print("YOU MADE", n*8, "DOLLARS A WEEK")
elif n<= 50 and n>0 :
    y=40*8+((n-40)*9)
    print("YOU MADE", y, "DOLLARS A WEEK")
elif n<168 and n>50 :
    y=40*8+10*9+((n-50)*10)
    print("YOU MADE", y, "DOLLARS A WEEK")
elif n<0 or n>168 :
    print("INVALID")
