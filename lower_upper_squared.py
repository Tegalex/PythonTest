lower = int(input("inserisci un valore basso nel range: "))
upper = int(input("inserisci un valore alto nel range: "))
for x in range (lower, upper):
    print ("il quadrato di {0} è {1}".format(x, x*x))
    