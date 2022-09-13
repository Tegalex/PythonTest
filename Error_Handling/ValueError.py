try:
    user_number = int(input("enter a number: "))
    print("your number is {0}".format(user_number))
except ValueError as e:
    print("you didn't enter a number! shame on you!")
    print(e)
print("fatto tutto!")