def reverse (string):
    out_string = ""
    length=len(string)
    for x in range(length,-1,-1):
        out_string = out_string + string[x]
    return out_string

 
