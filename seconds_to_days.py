#program podaje ilość sekund w dniach, godzinach, minutach, sekundach
response=int(input("give a number of seconds"))
days=int(response/(60*60*24))
hours=int((response-(days*60*60*24))/(60*60))
minutes=int(((response-(days*60*60*24)-(hours*60*60))/60))
seconds=int((response-(days*60*60*24)-(hours*60*60)-(minutes*60)))
print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
