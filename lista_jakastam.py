def time_converter(time):

    time_list=time.split(":")

    for first_element in time_list:
        if first_element in range (1,12):
            a=first_element+1
            return (first_element,":",a,"a.m")
        if  first_element==12:
            a=first_element+1
            return (first_element,":",a,"p.m")
        if first_element in range(13, 24):
            b=first_element-12
            return (b, ":",first_element, "p.m")

print(time_converter("12:30"))
