#project 8
#Jana Backman
#CIS 106
#Spring 2020

def validatingLengh(pw):
    flag =0
    if (len(myPassword)>=6):
        flag=1
    return flag

def validateUpper(pw):
    flag=0
    for i in pw:
        if (i.isupper()):
            flag=1
    return flag

def validateLower(pw):
    flag = 0
    for i in pw:
        if (i.islower()):
            flag = 1
    return flag

def validateDigit(pw):
    flag = 0
    for i in pw:
        if (i.isdigit()):
            flag=1
    return flag
    
#main()
loop = "x"

while (loop=="x"):
    print("Enter a pasword with at least 6 chars long,")
    print ("Must have at least one upper case letter,")
    print ("Must have at least one lower case letter,")
    print ("Must have at least one numeric digit: ")
    myPassword=input()


    print ("validating pasword...\n")

    gflag=validatingLengh(myPassword)
    if (gflag==0):
        print ("pasword to short need at least 6 chars")
     

    uflag= validateUpper(myPassword)
    if (uflag==0):
        print ("pasword does not have upper case letter, need at least one")
     

    lflag=validateLower(myPassword)
    if (lflag==0):
        print ("pasword does not have lower case letter, need at least one")
        

    dflag=validateDigit(myPassword)
    if (dflag==0):
        print("pasword missing a numeric digit")
      
    find=gflag+uflag+lflag+dflag
    if (find==4):
        print ("Validation completed -- password passes")
        loop = "a"
    else:
        print ("password not passes, try again\n")
        print("#################################\n")
        
    

