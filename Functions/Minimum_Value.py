def getNumber():
    #minimun_value = False
    minimum_value = 0
    done = False
    while not done:
        try:
            user_number = int(input("enter a number: "))
        except ValueError:
            print("you don't enter a number, shame on you")
            continue
        if minimum_value == False or user_number >= minimum_value:
            done =True
        else:
            print("your number was too low")
            print("the minimum value is {0}".format(minimum_value))
    return user_number