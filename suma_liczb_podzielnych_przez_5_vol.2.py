#suma liczb podzielnych przez 5
x=1
suma=0
while x<101 :
    if x%5==0 :#liczba podzielna przez 5
        suma=suma+x#suma liczb podzielnych przez 5
    x=x+1
print(suma)

#silnia liczb od 1 do n
# Type your code here
my_str = "university"
count = 0
for char in my_str:
    count = count + 1
    if char == "e":
        break  
print(count)
