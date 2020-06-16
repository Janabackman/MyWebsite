#project 7
#Jana Backman
#CIS 106
#Spring 2020


def printList(day, degree):
    print (day,":", degree)

def findMinMax(day, degree):
    indexMax = degree.index(max(degree))
    indexMin = degree.index(min(degree))
    print("The higer degree", max(degree), "on",day[indexMax])
    print("The lower degree", min(degree), "on",day[indexMin])

def average(degree):
    total = 0
    for x in degree:
        total += x
    average = total/(len(degree))
    print ("The average degree is: %.0f"%average)

#main()
days= ["Monday", "Tuesday","Wednsday","Thursday","Friday", "Saturday","Sunday"]
degrees=[42, 45, 86, 75, 43, 73, 29]

for i in range(0, len(days)):
    printList(days[i], degrees[i])

findMinMax(days,degrees)

average(degrees)
