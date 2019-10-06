n=int(input("daj liczbe"))
if n<=2:
    print( False)
elif n>=3:
    if n%2!=0:
        print (True)
    if n%2==0:
        print (False)
