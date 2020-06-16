#project 6
#Jana Backman
#CIS 106
#3/11/2020

def writefile():
    #writing to file
    #open filehandle
    fileHandle= open("names.txt", "w")
    loop = 1
    #use filehandle
    myName = input("Enter a name: ")
    fileHandle.write(myName + "\n")
    print("File has been written")
    while (loop == 1):
        option = input("Enter Y to continue and N when finish ")
        option= option.upper()
        if (option=="Y"):
            myName = input("Enter a name: ")
            fileHandle.write(myName+ "\n")
            print("File has been written")
        elif(option=="N"):
            print("Finish entering names")
            loop = 0
        else:
            print("WRONG option enter only Y or N")#end while
    #close filehandle
    fileHandle.close()

def readfile():
    #read from file
    fileName= input ("Enter name of file to read: ")
    #open filehandle
    fileHandle2= open(fileName, "r")
    #use filehandle
    line= fileHandle2.readline()
    count = 1
    while(line!=""):
        line = line.rstrip("\n")
        print (count,".",line)
        line = fileHandle2.readline()
        count+=1
        #end while
    #close filehandle
    fileHandle2.close()

    
#main()
try:
    print ("1. Write to file")
    print ("2. Read from file")
    print ("3. Exit")
    loop2 = "A"

    while (loop2=="A"):
        x= input("Enter your choice: ")
        if (x=="1"):
            writefile()
        elif(x=="2"):
            readfile()
        elif(x=="3"):
            loop2 = "x"
        else:
            print("That option does not exist, choose another one ")
    print("END PROGRAM")

except IOError:
    print("An error occure, The name of the file enter does not exist")
