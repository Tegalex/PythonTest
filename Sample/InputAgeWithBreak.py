age = int(input("Enter your age: "))
counter = 1
while age < 0 or age > 150:
    print("That was input #{0}, and you tried to trick me.".format(counter))
    age = int(input("Enter your age: "))
    counter = counter + 1
    if counter >= 5:
        age = 0
        break
print("Number of times that I had to ask you: {0}".format(counter))
if age == 0:
    print("You didn't follow the rules, and I am sad.")
else:
    print("Alright, you're {0} years old.".format(age))