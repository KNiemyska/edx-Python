n=int(input("daj liczbe"))
for x in range (1,n+1):
    print("%45s"%(x*"*"),x*"*")
for x in range (n-1,0,-1):
    print("%45s"%(x*"*"),x*"*")
