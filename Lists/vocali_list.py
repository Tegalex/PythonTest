import sys


vocali_list = ["a","e","i","o","u"]
lettera = input("Inserisci una lettera: ")

if lettera in vocali_list:
    print("la lettara {0} è una vocale. Ben fatto!".format(lettera))
else:
    print("la lettara {0} è una consonante. Ben fatto!".format(lettera))
    sys.exit()