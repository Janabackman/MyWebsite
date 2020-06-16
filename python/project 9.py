#Jana Backman
#CIS 106
#project 9

roomNumber={"CIS 101":"3004","CIS 102":"4501","CIS 103":"6755","NT 110":"1244","CM 241":"1411"}
instructor={"CIS 101":"Fisher","CIS 102":"Rich","CIS 103":"Burke","NT 110":"Green","CM 241":"Lee"}
mettingTime={"CIS 101":"8:00am","CIS 102":"9:00am","CIS 103":"10:00am","NT 110":"11:00am","CM 241":"1:00pm"}


for key in roomNumber:
    print (key)

key= input("\nChoose one of the clases to get info about it: ")
key = key.upper()

if key in roomNumber:
    print("Class room:",roomNumber.get(key, "--"))
    print ("Instructor:",instructor.get(key, "--"))
    print ("Metting Time:",mettingTime.get(key,"--"))
else:
    print ("Class not found")
