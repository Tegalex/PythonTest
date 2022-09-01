num = int(input("inserisci un numero: "))
if num > 0:
    print("è un numero positivo!")
    print("è maggiore di zero")
    print(f"il tuo numero è {num}".format(num))
elif num <0:
    print("il numero è negativo")
    print("è minore di zero")
    print(f"il tuo numero è {num}".format(num))
else:
    print("il numero non è nè positivo, nè negativo")
    print("è minore uguale a zero")
    print(f"il tuo numero è {num}".format(num))
print("Fatto tutto!")