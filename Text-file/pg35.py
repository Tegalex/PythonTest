input_file = open("pg35.txt", "r")
lines = input_file.readlines()
print("the input file has {0} lines of text".format(len(lines)))
print(lines[0])
for x in range (34,49):
    print("{0}: {1}".format(x, lines[x]), end="")
print("fatto tutto")