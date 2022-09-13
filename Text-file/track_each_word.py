input_file = open("pg35.txt", "r")
words = {}
for line in input_file:
    new_string = ""
    for x in line:
        if x.isalpha() or x == " ":
            new_string = "{0}{1}".format(new_string, x.lower())
    while new_string.find(" ") >=0:
        new_string = new_string.replace(" "," ")
    new_string=new_string.strip()
    if len(new_string) > 0:
        for word in new_string.split(" "):
            if word in words:
                words[word] +=1
            else:
                words[word] = 1
words_keys = sorted(words)
output_file = open("output.txt", "w")
output_file.write("There are {0} words in the file.\n".format(len(words)))
output_file.write("Some of the words in your file are:\n")
for key in words_keys:
    output_file.write("{0}: {1}\n".format(key, words[key]))
output_file.close()