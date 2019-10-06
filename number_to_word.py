n=int(input('please enter an integer between 1 and 9999: '))
if n>=1000:
    tysiace=int(n//1000)
    print(tysiace)
    setki=int(((n%(tysiace*1000))//100))
    print(setki)
    jednosci=int(((n%(tysiace*100))//10))
    print(jednosci)
