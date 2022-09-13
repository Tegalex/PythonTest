input_string = input("enter a string: ")
new_string = ""
for x in input_string:
    if x.isalpha()  or x == " ":
        new_string = "{0}{1}".format(new_string, x.lower())
while new_string.find(" ") >=0:
    new_string = new_string.replace(" ", " ")
new_string = new_string.strip()
words = new_string.split(" ")
words.sort()
print("the words in your string are: ")
print(words)