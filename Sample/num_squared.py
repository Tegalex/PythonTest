while True:
    num =int(input("inserisci un numero positivo, o 0 per uscire: "))
    if num<0:
        print("solo numeri positivi, grazie")
        continue
    elif num == 0:
        print("Ok, esci..")
        break
    num_squared = num *num
    print("{0} times {0} is {1}.".format(num, num_squared))
print("fatto tutto!")