# This program prints every character
# of the string
for char in "computer" :
    print(char)
print("Finished the for loop \n")
# This program shows the use of continue
# statement ina for loop

for char in "computer" :
    if char == "p" :
        continue
    print(char)
print("Finished the for loop with a continue \n")

# This program shows the use of break
# statement in a for loop

for char in "computer" :
    if char == "p" :
        break
    print(char)
print("Finished the for loop with a break")


my_list = [6, 5, 7, 2, 3, 5, 7, 8] 
count = 0
for number in my_list:
    if number == 5 or number == 7:
        continue
    else:
        count = count + number
    print(count)
