#suma liczb od 1 do 101 podzielnych przez 5

x=0
count=0
while x <= 101:
    if x%5==0:
        count = count+x
    x=x+1
print(count)


#prints the sum of every third numbers from 1 to 1001
x = 1
count = 0
iteration=0
while x < 101:
    count = count +x
    x = x + 3
    iteration=iteration+1
    print("iteracja",iteration, "liczba",count)
print(count)

#moje rozwiązanie
x=1
count=0
iteration=0
while x<=101 :
    count=count+x
    x=x+3
    iteration=iteration+1
    print("iteracja",iteration, "liczba",count)
print(count)
