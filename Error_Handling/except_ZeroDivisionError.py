done = False
while not donw:
    try:
        user_number = int(input("enter a number other than zero: "))
        division = 10 / user_number
        done =True
    except ValueError:
        print("you didn't enter a number, shame on you")
    except ZeroDivisionError:
        print("a number other than zero, please")
print("10 dived by {0} is {1}".format(user_number, 10/user_number))