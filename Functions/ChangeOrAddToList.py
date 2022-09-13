def noChangeList(yourList):
    yourList = []
    
def addToList(yourList):
    yourList.append(25)
    yourList.append(70)
    yourList.remove(yourList[0])

myList = [3, 5, 9, 12, 99]

print("original myList: {0}".format(myList))

noChangeList(myList)
print("Unchanged myList: {0}".format(myList))

addToList(myList)
print("modify myList: {0}".format(myList))