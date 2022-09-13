input_file = open("pg35.txt", "r")
words = []
for line in input_file:
    new_string = ""
    for x in line:
        if x.isalpha() or x == " ":
            new_string = "{0}{1}".format(new_string, x.lower())
        else:
            new_string = "{0} ".format(new_string)
    while new_string.find(" ") >= 0:
        new_string = new_string.replace(" ", " ")
    new_string = new_string.strip()
    if len(new_string) > 0:
        for word in new_string.split(" "):
            words.append(word)
words.sort()
print("There are {0} words in the file.".format(len(words)))
print("Some of the words in your file are:")
print(words[:10])
print(words[10000:10010])