age = int(input("Enter your age: "))
counter = 1
while age < 0 or age > 150:
    print("That was input #{0}, and you tried to trick me.".format(counter))
    age = int(input("Enter your age: "))
    counter = counter + 1
print("Alright, you're {0} years old.".format(age))
print("Number of times that I had to ask you: {0}".format(counter))
