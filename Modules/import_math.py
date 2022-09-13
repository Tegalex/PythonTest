import math

def getNumber(minimum_value=False, input_text="Enter a number: "):
    done = False
    while not done:
        try:
            user_number = int(input(input_text))
        except ValueError:
            print("You didn't enter a number! Shame on you.")
            continue
        if minimum_value == False or user_number >= minimum_value:
            done = True
        else:
            print("Your number was too low!")
            print("The minimum value is {0}.".format(minimum_value))
    return user_number

user_number = getNumber(minimum_value=0, input_text="Enter a number to obtain the square root: ")
print("The square root of {0} is {1}.".format(user_number, math.sqrt(user_number)))