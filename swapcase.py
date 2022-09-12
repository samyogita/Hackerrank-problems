def swap_case(s):
    string=''
    for a in s:
        if(a.isupper()==True):
            string=string+(a.lower())
        elif(a.islower()==True):
            string=string+(a.upper())
        elif(a.isspace()==True):
            string=string+a
        else:
            string=string+a
    
    return string

