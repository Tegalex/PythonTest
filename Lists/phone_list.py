phone_list = [5555593, 5554710, 5554913, 5555772, 5559913]

start_list = int(input("inserisci un primo numero di telefono: "))
end_list = int(input("inserisci un ultimo numero di telefono: "))

for phone in phone_list:
    if phone >= start_list and phone <= end_list:
        print("in numero di telefono nel range: {0}".format(phone))
    else:
        print("Ha sbagliato ad inserire il range, non abbiamo numeri da mostrarti")
    break
