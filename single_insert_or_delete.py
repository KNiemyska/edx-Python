def single_insert_or_delete(s1,s2):
    s1=s1.lower().split()
    s2=s2.lower().split()
    if s1==s2:
        return(0)
    for character in range (0, len(s1),1):

        if s1[character]!=s2[character]:  #inserting   
            s11=s1[0:character]+s2[character]+s1[character:len(s1)]
            if s11==s2:
                return( 1 )
                break
            if s11!=s2:
                if s1[character]!=s2[character]:#delete
                    s1=s1[0:character]+s1[character+1:len(s1)]
                    if s1==s2:
                        return( 1 )
                        break   
    else:
        return 2
 
