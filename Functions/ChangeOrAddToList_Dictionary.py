def noChangeDict(yourDict):
    yourDict = {}

def addToDict(yourDict):
    yourDict.clear()
    yourDict["Alexander"] = True

myDict = {"test": 35, "foo": 21, "bar": 5}

print("Original myDict: {0}".format(myDict))

noChangeDict(myDict)
print("Unchanged myDict: {0}".format(myDict))

addToDict(myDict)
print("Modified myDict: {0}".format(myDict))